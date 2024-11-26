from main.d_vs_c.config.data_ingestion_config import ConfigManeger
from main.d_vs_c.components.download_data import DataIngestion
from main.d_vs_c import logger

class data_inges_pipeline:

    def __init__(self):
        pass

    def main(self):
            confi = ConfigManeger()
            x = confi.get_data_download_config()
            data = DataIngestion(config=x)
            downloaded_path = data.download_datafile()
            data.move_data_file(downloaded_path)
            # data.move_data_file("C:\\Users\\Public\\Deep Learning\\datasets\\PetImages")

if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Stage Data Ingestion Process Started...')
        obj = data_inges_pipeline()
        obj.main()
        logger.info('>>>>>>>>>>>>>>>Data Ingestion Proess Completed........')
        logger.info('<<<<<<<<<<<<<<<<<<<<')


    except Exception as e:
        raise e
