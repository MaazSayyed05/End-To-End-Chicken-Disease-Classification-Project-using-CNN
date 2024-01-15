import os
from chicken_disease_classification import logger

from chicken_disease_classification.config.configuration import ConfigurationManager

from chicken_disease_classification.entity.config_entity import DataIngestionConfig

from chicken_disease_classification.components.data_ingestion import DataIngestion

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # data_ingestion.download_data()
        # download datasets form kaggle as given in notebook.




if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>> {STAGE_NAME} Started <<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>> {STAGE_NAME} Complted <<<<<<<')

    except Exception as e:
        logger.error(f'>>>>>>>> {STAGE_NAME} Failed <<<<<<<')
        raise e