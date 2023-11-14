from plantDiseaseDetection.constants import *
from plantDiseaseDetection.components.data_ingestion import DataIngestion
from plantDiseaseDetection.components.prepare_base_model import PrepareBaseModel
from plantDiseaseDetection.components.prepare_callback import PrepareCallback
from plantDiseaseDetection.components.model_training import Traing
from plantDiseaseDetection.components.model_evaluation import Evaluate
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

            # Prepare Callbacks
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callback = PrepareCallback(config=prepare_callbacks_config)
            callback_list = prepare_callback.get_tb_ckpt_callback()

            # Model Training
            training_config = config.get_training_config()
            training = Traing(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list = callback_list)

            #Model Evaluation
            val_config = config.get_validation_config()
            evaluation = Evaluate(config=val_config)
            evaluation.evaluation()
        
        except Exception as e:
            raise e
