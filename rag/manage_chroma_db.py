import argparse
import os
import shutil
import logging
from dotenv import load_dotenv
from langchain_community.document_loaders import S3DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
import logging

# These three lines swap the stdlib sqlite3 lib with the pysqlite3 
#__import__('pysqlite3')
#import sys
#sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Configuration for MinIO from environment variables
MINIO_ENDPOINT = os.getenv("AWS_S3_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
MINIO_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
MINIO_BUCKET_NAME = "lakehouse"

# Ollama configuration
OLLAMA_HOST = os.getenv("OLLAMA_HOST")
print("OLLAMA_HOST =", os.getenv("OLLAMA_HOST"))

def main():
    parser = argparse.ArgumentParser(description="Populate and query the Chroma database.")
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    parser.add_argument("--query", type=str, help="Query text for retrieval.")
    args = parser.parse_args()

    if args.reset:
        logging.info("Clearing Database")
        clear_database()

    if args.query:
        logging.info(f"Querying the database with text: {args.query}")
        answer, sources = run_query(args.query)
        print("Answer:", answer)
        print("Sources:", sources)
    
    else:
        logging.info("Populating the database with documents")
        documents = load_documents()
        chunks = split_documents(documents)
        add_to_chroma(chunks)

def load_documents():
    logging.info("Loading documents from MinIO")
    directory_loader = S3DirectoryLoader(
        bucket=MINIO_BUCKET_NAME,
        prefix="documents",
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=MINIO_ACCESS_KEY, 
        aws_secret_access_key=MINIO_SECRET_KEY
    )
    documents = directory_loader.load()
    logging.info(f"Loaded {len(documents)} documents")
    return documents

def split_documents(documents: list[Document]):
    logging.info("Splitting documents into chunks")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    logging.info(f"Split into {len(chunks)} chunks")
    return chunks

def get_embedding_function():
    embeddings = OllamaEmbeddings(base_url=OLLAMA_HOST, model="nomic-embed-text")
    return embeddings

def add_to_chroma(chunks: list[Document]):
    logging.info("Adding chunks to Chroma database")
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )
    chunks_with_ids = calculate_chunk_ids(chunks)
    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    logging.info(f"Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = [chunk for chunk in chunks_with_ids if chunk.metadata["id"] not in existing_ids]

    if new_chunks:
        logging.info(f"Adding {len(new_chunks)} new documents")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        logging.info("No new documents to add")

def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id

    return chunks

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    logging.info("Database cleared")


def run_query(query_text: str) -> tuple[str, list[str]]:
    logging.info("Preparing the DB for query")
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    logging.info("Searching the DB")
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(base_url=OLLAMA_HOST, model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    return response_text, sources

if __name__ == "__main__":
    main()
    logging.getLogger().setLevel(logging.ERROR)
