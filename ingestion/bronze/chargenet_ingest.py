from ingestion.utils.spark_utils import create_spark_session
from ingestion.utils.data_ingestor import DataIngestor
from ingestion.utils.config_loader import ConfigLoader
from ingestion.utils.file_path_manager import FilePathManager

if __name__ == "__main__":
    config = ConfigLoader()
    spark = create_spark_session()
    ingestor = DataIngestor(spark)
    path_manager = FilePathManager(config.base_data_dir, config.lakehouse_s3_path)

    # Ingest chargenet_stations.json to the Bronze layer
    stations_file = path_manager.get_local_file_path("chargenet_stations", "json")
    ingestor.ingest_file_to_bronze(stations_file, "chargenet", "stations", "json")

    # Ingest chargenet_charging_sessions.json to the Bronze layer
    sessions_file = path_manager.get_local_file_path("chargenet_charging_sessions", "json")
    ingestor.ingest_file_to_bronze(sessions_file, "chargenet", "charging_sessions", "json")