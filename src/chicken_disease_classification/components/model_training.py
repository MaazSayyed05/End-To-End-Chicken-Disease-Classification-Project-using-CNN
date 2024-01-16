
import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time

from pathlib import Path

from chicken_disease_classification.entity.config_entity import TrainingConfig
from chicken_disease_classification.entity.config_entity import PrepareCallbacksConfig

class Training:
    def __init__(
        self,
        config: TrainingConfig):

        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )


    def train_valid_generator(self):

        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )

        # test_data_generator_kwargs = dict(
        #     rescale = 1./255,
        #     validation_split = 0.20
        # )



        data_flow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            # shuffle = True,
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


        # test_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
        #     **test_data_generator_kwargs
        # )


        # self.test_generator = test_data_generator.flow_from_directory(
        #     data = self.valid_generator,
        #     subset = 'validation',
        #     shuffle = False,
        #     class_mode='categorical',
        #     **data_flow_kwargs
        # )



        if self.config.params_is_augmented:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                horizontal_flip = True,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                **data_generator_kwargs
            )

        else:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                **data_generator_kwargs
            )
        
        self.train_generator = train_data_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'training',
            shuffle = True,
            class_mode='categorical',
            **data_flow_kwargs
        )

    

    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)
    

    def train(self,callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size

        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size 


        self.model.fit(
            self.train_generator,
            steps_per_epoch = self.steps_per_epoch,
            epochs = self.config.params_epoch,
            validation_data = self.valid_generator,
            validation_steps = self.validation_steps,
            callbacks = callback_list
        )


        self.save_model(
            path = self.config.trained_model_path,
            model =self.model
        )


