from ingestion.utils.spark_utils import create_spark_session
from ingestion.utils.config_loader import ConfigLoader
from ingestion.utils.file_path_manager import FilePathManager
from ingestion.utils.document_data_ingestor import DocumentDataIngestor
import os

def format_s3_bucket_name(s3_path):
    # Remove s3a:// prefix if present
    if s3_path.startswith("s3a://"):
        s3_path = s3_path[6:]
    # Remove trailing slash if present
    return s3_path.rstrip('/')

if __name__ == "__main__":
    config = ConfigLoader()
    ingestor = DocumentDataIngestor(s3_bucket=format_s3_bucket_name(config.lakehouse_s3_path),
                            aws_access_key_id=config.aws_access_key_id,
                            aws_secret_access_key=config.aws_secret_access_key,
                            aws_s3_endpoint=config.aws_s3_endpoint)

    # Ingest all PDF documents in a folder to the Bronze layer
    pdf_folder = os.path.join(config.base_data_dir, "documents")

    # Iterate through all files in the folder and ingest each PDF
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(pdf_folder, filename)
            ingestor.ingest_document_to_bronze(pdf_file, "documents")
