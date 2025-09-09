from src.mlProject.components.data_validation import DataValiadtion
from src.mlProject import logger


class DataValidationPipeline():
    def __init__(self):
        pass
    def main(self):
        data_validation = DataValiadtion()
        data_validation.validate_all_columns()
