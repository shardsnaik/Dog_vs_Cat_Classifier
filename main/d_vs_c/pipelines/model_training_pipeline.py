from main.d_vs_c.config.model_training_config import ConfigManeger
from main.d_vs_c.components.buid_train_model import Datasets, plot_nd_save
from main.d_vs_c import logger

class train_save_pipeline:

    def __init__(self):
        pass

    def main(self):
        config  = ConfigManeger()
        confi = config.bilding_model_config()
        obj1 = Datasets(config=confi, params=confi)
        train, test = obj1.datasets_()

        train_ds = train.map(obj1.process)
        test_ds = test.map(obj1.process)
        model = obj1.model()
        model.summary()
        history = obj1.run_model(model, train_ds, test_ds)

        obj2 = plot_nd_save(config=confi, params=confi, history=history, model=model)
        obj2.plot_()
        obj2.save_model()


if __name__ == '__main__':
    try:
        logger.info('<<<<<<<<<  The Model Training Pipeline Started >>>>>>>>')
        obj = train_save_pipeline()
        obj.main()
        logger.info('<<<<<<<<<  The Model Training Pipeline Finished >>>>>>>>')
    except Exception as e:
        raise e