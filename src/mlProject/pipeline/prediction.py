import numpy as np
import joblib
import pandas as pd
from mlProject.constants import *
from src.mlProject.utils.common import read_yaml


class PredictionPipeline:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
    
        self.model = joblib.load(self.config.model_evaluation.model_path)

    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction
