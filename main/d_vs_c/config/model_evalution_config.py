from main.d_vs_c.funtions.comon_funtn import read_yaml, create_directories, save_json_file
from main.d_vs_c.utils import *

class ConfigManeger:
    def __init__(self, config_path=config_file,
                 param_path= params_file):
        self.config = read_yaml(config_path)
        self.parmas = read_yaml(params_file)

        create_directories([self.config.artifacts_folder])

    def get_evalution_config(self):
        config = self.config.trained_model

        create_directories([config.trained_model_path])

        eval_config = {
            'test_dir' : Path(config['test_dir']),
            'trained_model_path' : Path(config['trained_model_path']),
            'model_name' : config['trained_model_name']
        }
        return eval_config



        