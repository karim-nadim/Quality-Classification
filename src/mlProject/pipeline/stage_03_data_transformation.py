from src.mlProject.components.data_transformation import DataTransformation
from src.mlProject import logger


class DataTransformationPipeline():
    def __init__(self):
        pass
    def main(self):
        data_transformation = DataTransformation()
        data_transformation.train_test_spliting()
