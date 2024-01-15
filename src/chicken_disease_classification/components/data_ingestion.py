
import os
import urllib.request as request
import zipfile
from chicken_disease_classification import  logger
from chicken_disease_classification.utils.common import download_kaggle_dataset, get_size


from chicken_disease_classification.entity.config_entity import DataIngestionConfig




class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        #         # Example usage:
        # # Replace the placeholders with your Kaggle dataset details and API credentials

        # download_kaggle_dataset(
        #     dataset_name='your-username/dataset-name',
        #     output_folder='/path/to/local/folder',
        #     kaggle_username='your-kaggle-username',
        #     kaggle_key='your-kaggle-api-key'
        # )

        try: 
            download_kaggle_dataset(
                username = self.config.kaggle_username,
                dataset_name = self.config.dataset_name,
                output_path = self.config.unzip_dir
            )

            logger.info(f'Downloaded {self.config.dataset_name} to {self.config.unzip_dir} Successfully.')  

        except Exception as e:
            logger.error(f'Failed to download {self.config.dataset_name} to {self.  config.unzip_dir}. \nError: {e}')
    
    



