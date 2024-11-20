from main.d_vs_c.funtions.comon_funtn import read_yaml, create_directories
from main.d_vs_c.utils import *


class ConfigManeger:

    def __init__(self, config_path = config_file,
                 param_path= params_file):
        self.config = read_yaml(config_path)
        self.params = read_yaml(param_path)

        create_directories([self.config.artifacts_folder])

    def bilding_model_config(self):
        config = self.config.trained_model
        create_directories([config.trained_model_path])

        # bild_model = (
        #     train_dir = Path(config.train_dir),
        #     test_dir= Path(config.test_dir),
        #     batch_size =self.params.batch_size,
        #     seed= self.params.seed
        # )
        bild_model = {
            'train_dir' : Path(config['train_dir']),
            'test_dir': Path(config['test_dir']),
            'batch_size': self.params['batch_size'],
            'seed': self.params['seed'],
            'image_size': self.params['image_size'],
            'conv_first_layer': self.params['conv_first_layer'],
            'conv_sec_layer': self.params['conv_sec_layer'],
            'conv_third_layer': self.params['conv_third_layer'],
            'conv_fourth_layer': self.params['conv_fourth_layer'],
            'input_shape': self.params['input_shape'],
            'kernel_size': self.params['kernel_size'],
            'pool_size': self.params['pool_size'],
            'strides': self.params['strides'],
            'dropout_rate': self.params['dropout_rate'],
            'dense_first_layer': self.params['dense_first_layer'],
            'dense_second_layer': self.params['dense_second_layer'],
            'output_layer': self.params['output_layer'],
            'l2_regularization': self.params['l2_regularization'],
            'optimizer': self.params['optimizer'],
            'loss': self.params['loss'],
            'epochs': self.params['epochs']
        }
        return bild_model

        