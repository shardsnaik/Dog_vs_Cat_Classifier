from main.d_vs_c.config.data_preprocess_config import ConfigManeger
from main.d_vs_c.components.data_preprocess import Pre_process_img
from main.d_vs_c import logger

class preprocess_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
       obj = ConfigManeger()
       config = obj.pre_process_config()
       pre = Pre_process_img(config=config)
       pre.process_img()
       logger.info ('|||||||||||   Removing Images   |||||||||')
       pre.remove_img()



if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Images Preprocess Pipline has Started  >>>>>>>>>>>>>')
        obj = preprocess_pipeline()
        obj.main()
        logger.info('  <<<<<<<<<<<<<<<<<< Images Preprocess Pipline has Finished  <<<<<<<<<<<<<<<<<<.')
    except Exception as e:
        raise e