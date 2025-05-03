from Model_Configuration.Model_Constants import *
from Utils.utils import read_yaml, create_directories
from Model_Configuration.Model_Entitys.model_config_entity import DataIngestionConfig

class Configuration:
    def __init__(self, config_file_path: Path = CONFIG_FILE_PATH, params_file_path: Path = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_file_path)
        #self.params = read_yaml(params_file_path)
        #self.schema = read_yaml(SCHEMA_FILE_PATH)
       #cls
       #  self.project_name = self.config.project_details.project_name

        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig :
    
        config = self.config["data_ingestion"]
        create_directories([config.root_dir_artifacts, config.root_dir_data])

        data_ingestion_config = DataIngestionConfig(
            root_dir_artifacts=config.root_dir_artifacts,
            root_dir_data=config.root_dir_data,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config