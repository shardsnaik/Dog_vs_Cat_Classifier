from main.d_vs_c.config.data_spliting_config import Preprocess
from main.d_vs_c.components.split_move_data import split_and_move
from main.d_vs_c import logger

class data_split_and_move:
    def __init__(self) -> None:
        pass

    def main(self):
        obj = Preprocess()
        con = obj.splting_data_config()
        split = split_and_move(config= con, params= con)
        split.spliting_the_data()
        split.getting_size()

if __name__ == '__main__':
    try:
        logger.info ('>>>>>>>>>>>>>>>>  Split and Move Pipline has Started  >>>>>>>>>>>>>')
        obj = data_split_and_move()
        obj.main()
        logger.info('  <<<<<<<<<<<<<<<<<< Split and Move Pipline has Finished  <<<<<<<<<<<<<<<<<<.')
    except Exception as e:
        raise e