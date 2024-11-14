from sklearn.model_selection import train_test_split
import shutil
from main.d_vs_c.funtions.comon_funtn import read_yaml, create_directories
from main.d_vs_c import logger
from main.d_vs_c.utils import *

class Preprocess:
    def __init__(self,
                 confi_path = config_file,
                 param_path = params_file):
        self.config = read_yaml(confi_path)
        self.params = read_yaml(param_path)

        create_directories([self.config.artifacts_folder])

    def splting_data_config(self):
        config = self.config.preproccessed_data
        create_directories([config.datasets_dir])

        split_config = {
            'train_dir': Path(config['train_dir']),
            'test_dir': Path(config['test_dir'])
        }

        return split_config