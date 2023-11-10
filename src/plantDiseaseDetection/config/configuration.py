from plantDiseaseDetection.constants import *
from plantDiseaseDetection.utils import read_yaml, create_directories
from plantDiseaseDetection.entity import DataIngestionConfig

# Configuration Manager
class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig: 
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_URL,
            raw_dataset_dir = config.raw_dataset_dir,
            dataset_dir = config.dataset_dir
        )

        return data_ingestion_config