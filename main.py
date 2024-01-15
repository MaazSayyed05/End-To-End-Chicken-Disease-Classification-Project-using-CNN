
from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} Started <<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} Complted <<<<<<<')

except Exception as e:
    logger.error(f'>>>>>>>> {STAGE_NAME} Failed <<<<<<<')
    raise e


