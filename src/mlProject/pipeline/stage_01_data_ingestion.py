from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject import logger


class DataIngestionTrainingPipeline():
    def __init__(self):
        pass
    def main(self):
        data_ingestion = DataIngestion()
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
