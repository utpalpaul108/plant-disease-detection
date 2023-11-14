from plantDiseaseDetection.entity import EvaluationConfig
from plantDiseaseDetection.utils import save_json
from pathlib import Path
import tensorflow as tf


class Evaluate:

    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):
        
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'validation',
            shuffle = False,
            **dataflow_kwargs
        )

    def load_model(self, path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        score = model.evaluate(self.valid_generator)
        save_json(path = self.config.evaluation_score_path, data={'loss': score[0], 'accuracy': score[1]})
