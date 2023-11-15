import tensorflow as tf
from tensorflow import keras
from plantDiseaseDetection.config import ConfigurationManager
from plantDiseaseDetection.constants import *
from plantDiseaseDetection.utils import read_yaml
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

class PlantDisease:

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigurationManager()
        self.params = read_yaml(PARAMS_FILE_PATH)
        self.training_config = self.config.get_training_config()
        self.data_ingestion_config = self.config.get_data_ingestion_config()

    def _get_prediction_classes(self):
        classes = sorted(os.listdir(self.data_ingestion_config.dataset_dir))
        class_id_to_label = {i: class_name for i, class_name in enumerate(classes)}
        return class_id_to_label
    
    def predict(self):
        
        # Load Model
        model = load_model(self.training_config.trained_model_path)

        img_name = self.filename
        target_img_size = tuple(self.params.IMAGE_SIZE[:2])
        test_image = load_img(img_name, target_size = target_img_size)
        
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        predictions = model.predict(test_image)
        result = np.argmax(predictions)

        prediction_classes = self._get_prediction_classes()
        predicted_class_label = prediction_classes[result]
        
        return [{'image': predicted_class_label}]

