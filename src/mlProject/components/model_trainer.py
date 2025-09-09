from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
import pandas as pd
import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib

class ModelTrainer:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        create_directories([self.config.model_trainer.root_dir])

    
    def train(self):
        train_data = pd.read_csv(self.config.model_trainer.train_data_path)
        test_data = pd.read_csv(self.config.model_trainer.test_data_path)


        train_x = train_data.drop([self.schema.TARGET_COLUMN.name], axis=1)
        test_x = test_data.drop([self.schema.TARGET_COLUMN.name], axis=1)
        train_y = train_data[[self.schema.TARGET_COLUMN.name]]
        test_y = test_data[[self.schema.TARGET_COLUMN.name]]


        lr = ElasticNet(alpha=self.params.ElasticNet.alpha, 
                        l1_ratio=self.params.ElasticNet.l1_ratio, 
                        random_state=42)

        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.model_trainer.root_dir, self.config.model_trainer.model_name))

