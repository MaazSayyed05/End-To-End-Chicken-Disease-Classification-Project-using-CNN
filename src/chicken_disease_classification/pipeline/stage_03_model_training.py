
from chicken_disease_classification.config.configuration import ConfigurationManager

from chicken_disease_classification.components.prepare_base_model import PrepareBaseModel

from chicken_disease_classification.components.prepare_callbacks import PrepareCallbacks


from chicken_disease_classification.components.model_training import Training


from chicken_disease_classification import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
            callbacks_list = prepare_callbacks.get_tb_ckpt_callbacks
#           ----------------------------------------------------------------
            training_config = config.get_training_data_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            # training.train(callback_list=callbacks_list)

        except Exception as e:
            raise e



