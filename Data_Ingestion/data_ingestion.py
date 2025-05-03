import os
import urllib.request as request
from Logger import logger
import zipfile
from Model_Configuration.Model_Entitys.model_config_entity import DataIngestionConfig
from Model_Configuration.configuration import Configuration


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Download the file from the source URL and save it locally.
        """
        logger.info(f"Downloading file from {self.config.source_URL} to {self.config.local_data_file}")
        if not os.path.exists(self.config.local_data_file):
            request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"File downloaded successfully to {self.config.local_data_file}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        data_dir = self.config.root_dir_data
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            zip_ref.extractall(data_dir)
    

if __name__ == "__main__":
    try:
        config=Configuration()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        logger.exception(e)
        raise e