
from chicken_disease_classification import logger
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} Started <<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} Complted <<<<<<<')

except Exception as e:
    logger.error(f'>>>>>>>> {STAGE_NAME} Failed <<<<<<<')
    raise e



STAGE_NAME = 'Prepare Base Model Stage'

try:
    logger.info(f'>>>>>>>> {STAGE_NAME} Started <<<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f'>>>>>>>> {STAGE_NAME} Complted <<<<<<<')

except Exception as e:
    logger.error(f'>>>>>>>> {STAGE_NAME} Failed <<<<<<<')
    raise e


