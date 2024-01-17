
import os
import tensorflow as tf
from pathlib import Path

from chicken_disease_classification.config.configuration import ConfigurationManager

from chicken_disease_classification.components.model_evaluation import Evaluation

from chicken_disease_classification import logger


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            eval = Evaluation(config = eval_config)
            # eval.evaluation()
            # eval.save_score()

        except Exception as e:
            raise e