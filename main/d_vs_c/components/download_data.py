import os
import kagglehub
from main.d_vs_c import logger
import shutil

class DataIngestion:
    def __init__(self, config):
        self.config  = config 

    def download_datafile(self):
        os.makedirs('artifacts/raw_data', exist_ok=True)
        try:
            logger.info('Downloading data from Kaggle has started...........')
            # Download latest version
            path = kagglehub.dataset_download(self.config['source_URL'])
            print("Path to dataset files:", path)

        except Exception as e:
            raise e
        return path
        
    def move_data_file(self, path):
        for filename in os.listdir(path):
            full_filename = os.path.join(path, filename)
            shutil.move(full_filename, self.config['source_dir'] )

        logger.info(f"File moved from {path} to {self.config['source_dir']}")



