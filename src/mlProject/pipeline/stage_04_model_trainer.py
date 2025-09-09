from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject import logger


class ModelTrainerPipeline():
    def __init__(self):
        pass
    def main(self):
        model_trainer = ModelTrainer()
        model_trainer.train()
