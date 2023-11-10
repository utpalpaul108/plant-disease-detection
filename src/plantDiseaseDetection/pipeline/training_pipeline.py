from plantDiseaseDetection.constants import *
from plantDiseaseDetection.components.data_ingestion import DataIngestion
from plantDiseaseDetection.config import ConfigurationManager
from pathlib import Path

class TrainingPipeline:
    def train(self):
        try:
            config = ConfigurationManager()
        
            # Data Ingestion
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
        
        except Exception as e:
            raise e
