from main.d_vs_c.funtions.comon_funtn import read_yaml, create_directories
from main.d_vs_c.utils import *


class ConfigManeger:
    def __init__(self, config_path = config_file,
                  params_path = params_file): 
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.config.artifacts_folder])

    def pre_process_config(self):
        config = self.config.preproccessed_data
        create_directories([config.datasets_dir])

        preprocess_config = {
            'datasets_dir': Path(config['datasets_dir']),
            'train_dir': Path(config['train_dir']),
            'test_dir': Path(config['test_dir']),
            'image_categories': self.config['image_categories'] 
        }

        return preprocess_config