from main.d_vs_c.utils import *
from main.d_vs_c.funtions.comon_funtn import read_yaml, create_directories

class ConfigManeger:
    def __init__(self,
                 config_path = config_file,
                  param_path = params_file ):
        self.config = read_yaml(config_path)
        self.params =read_yaml(param_path)

        create_directories([self.config.artifacts_folder])

    def get_data_download_config(self):
        config = self.config.downloading_data
        # print(config)

        create_directories([config.source_dir])
        download_config = {
            'source_dir': Path(config['source_dir']),
            'source_URL': config['source_URL']
        }


        return download_config