from main.d_vs_c.config.model_evalution_config import ConfigManeger
from main.d_vs_c.components.eval_model_mlflow import Evalution
from main.d_vs_c import logger
class Model_evalution_pipeline:
    
    def __init__(self):
        pass

    def main(self):
        obj = ConfigManeger()
        confi = obj.get_evalution_config()
        eval_obj = Evalution(confi, confi)
        eval_obj.laod_nd_eval()
        eval_obj.save_score()
        eval_obj.implementing_mlflow()


if __name__ == '__main__':
    try:
        logger.info('<<<<<<<<<  The Model Evalution Pipeline Started <<<<<<<<<<<<<  ')
        eval = Model_evalution_pipeline()
        eval.main()
        logger.info('>>>>>>>>>>>>   The Model Evalution Pipeline Fineshed Sucessfully......... >>>>>>>>')
    except Exception as e:
        raise e