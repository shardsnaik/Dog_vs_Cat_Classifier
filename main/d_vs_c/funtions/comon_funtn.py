import yaml
from pathlib import Path
from box import ConfigBox
import os
import logging
from ensure import ensure_annotations
import json

@ensure_annotations
def read_yaml(path: Path):
    # Open the YAML file
    with open(path) as file:
        try:
            # Load and return the YAML content
            data = yaml.safe_load(file)
            print(data)  # Optional: print to verify the content
            return ConfigBox(data)  # Return the loaded data
        except yaml.YAMLError as exc:
            print(exc)
            return None  # Return None if there's an error

@ensure_annotations
def create_directories(path_to_dirs:list, verbose=True):
    '''
    create the list of directorres

    '''
    for path in path_to_dirs:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logging.info(f'created directory at: {path}')

# read_yaml(Path('C:\\dog_vs_cat_clasifier\\config\\config.yaml'))

@ensure_annotations
def save_json_file(path: Path, data: dict):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")