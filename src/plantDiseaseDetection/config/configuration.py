from plantDiseaseDetection.constants import *
from plantDiseaseDetection.utils import read_yaml, create_directories
from plantDiseaseDetection.entity import DataIngestionConfig, PrepareBaseModelConfig

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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:

        config = self.config.prepare_base_model
        create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = config.root_dir,
            base_model_path = config.base_model_path,
            updated_base_model_path = config.updated_base_model_path,
            params_image_size = self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_dropout_rate = self.params.DROPOUT_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return prepare_base_model_config