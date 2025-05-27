import os
import logging
import boto3
from ingestion.utils.file_path_manager import FilePathManager

class DocumentDataIngestor:
    def __init__(self, s3_bucket: str = None, aws_access_key_id: str = None, aws_secret_access_key: str = None, aws_s3_endpoint: str = None):
        self.s3_bucket = s3_bucket
        self.s3_client = boto3.client('s3', 
                                      aws_access_key_id=aws_access_key_id, 
                                      aws_secret_access_key=aws_secret_access_key,
                                      endpoint_url=aws_s3_endpoint)

    def ingest_document_to_bronze(self, file_path: str, dataset_name: str):
        try:
            s3_key = dataset_name + '/' + os.path.basename(file_path)

            self.s3_client.upload_file(file_path, self.s3_bucket, s3_key)

            logging.info(f"Document {file_path} ingested successfully to s3://{self.s3_bucket}/{s3_key}")
        
        except Exception as e:
            logging.error(f"Error ingesting document to bronze: {e}")
            raise e
