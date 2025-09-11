from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories, save_json
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import dagshub

class ModelEvaluation:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        self.mlflow_uri = "https://dagshub.com/karim-nadim/Quality-Classification.mlflow"

        create_directories([self.config.artifacts_root])
        create_directories([self.config.model_evaluation.root_dir])


    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.model_evaluation.test_data_path)
        model = joblib.load(self.config.model_evaluation.model_path)

        test_x = test_data.drop([self.schema.TARGET_COLUMN.name], axis=1)
        test_y = test_data[[self.schema.TARGET_COLUMN.name]]


        mlflow.set_registry_uri(self.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        
        dagshub.init(repo_owner='karim-nadim', repo_name='Quality-Classification', mlflow=True)

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.model_evaluation.metric_file_name), data=scores)

            mlflow.log_params(self.params.ElasticNet)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")

    
