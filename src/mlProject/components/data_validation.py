import pandas as pd
from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
import os
from mlProject import logger

class DataValiadtion:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        create_directories([self.config.data_validation.root_dir])


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.data_validation.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.schema.COLUMNS.keys()

            
            for col in all_cols:
                if col not in all_schema or data[col].dtype != self.schema.COLUMNS[col]:
                    validation_status = False
                    with open(self.config.data_validation.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.data_validation.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e

