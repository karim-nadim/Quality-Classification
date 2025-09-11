from src.mlProject import logger
from src.mlProject.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        model_evaluation_config = ModelEvaluation()
        model_evaluation_config.log_into_mlflow()        


