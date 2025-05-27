from ingestion.utils.spark_utils import create_spark_session
from ingestion.utils.data_ingestor import DataIngestor
from ingestion.utils.config_loader import ConfigLoader
from ingestion.utils.file_path_manager import FilePathManager

if __name__ == "__main__":
    config = ConfigLoader()
    spark = create_spark_session()
    ingestor = DataIngestor(spark)
    path_manager = FilePathManager(config.base_data_dir, config.lakehouse_s3_path)

    # Ingest vehicle_health_data.json to the Bronze layer
    vehicle_health_file = path_manager.get_local_file_path("vehicle_health_data", "json")
    ingestor.ingest_file_to_bronze(vehicle_health_file, "vehicle_health", "logs", "json")