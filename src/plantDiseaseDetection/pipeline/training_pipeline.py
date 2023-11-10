from plantDiseaseDetection.constants import *
from plantDiseaseDetection.components.data_ingestion import DataIngestion
from plantDiseaseDetection.components.prepare_base_model import PrepareBaseModel
from plantDiseaseDetection.config import ConfigurationManager


class TrainingPipeline:
    def train(self):
        try:
            config = ConfigurationManager()
        
            # Data Ingestion
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.initiate_data_ingestion()

            # Prepare Base Model
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.initiate_prepare_base_model()
        
        except Exception as e:
            raise e
