
from chicken_disease_classification.constants import  *
from chicken_disease_classification.utils.common import  read_yaml, create_directories



from chicken_disease_classification.entity.config_entity import DataIngestionConfig



class ConfigurationManager:
    def __init__(
        self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        self.config = self.config.data_ingestion
        self.params = self.params.data_ingestion

        create_directories([self.config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = self.config.root_dir,
            source_url = self.config.source_url,
            unzip_dir = self.config.unzip_dir,
            kaggle_api_key = self.config.kaggle_api_key,
            dataset_name = self.params.dataset_name,
            kaggle_username = self.params.kaggle_username
        )

        return data_ingestion_config



