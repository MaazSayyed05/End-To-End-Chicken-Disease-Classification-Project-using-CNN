
from urllib.parse import urlparse
from chicken_disease_classification.utils.common import load_json, save_json
import tensorflow as tf

import os
from pathlib import Path

from chicken_disease_classification.entity.config_entity import EvaluationConfig



class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    

    def valid_generator(self):

        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30 
        )

        data_flow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )


        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'validation',
            shuffle = False,
            class_mode='categorical',
            **data_flow_kwargs

        )


    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self.valid_generator()
        self.score = model.evaluate(self.valid_generator)


    def save_score(self):
        scores = {'loss': self.score[0], 'accuracy': self.score[1]}
        save_json(path=Path('scores.json'), data=scores)
        






