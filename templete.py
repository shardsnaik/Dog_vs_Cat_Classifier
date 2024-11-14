from pathlib import Path
import os
import logging

list_of_files = [
    '.github/workflow/.gitkeep',
    'main/d_vs_c/__init.py',
    'main/d_vs_c/components/__init__.py', 
    'main/d_vs_c/utils/__init__.py', 
    'main/d_vs_c/config/__init__.py', 
    'main/d_vs_c/pipelines/__init__.py', 
    'main/d_vs_c/entities/__init__.py', 
    'main/d_vs_c/funtions/__init__.py', 
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirments.txt',
    'trials/trials_01.ipynb',
    'templates/index.html',
    '.gitignore'
]

for files in list_of_files:
    files = Path(files)
    print(files)
    file_dir, file_name = os.path.split(files)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info('Creating directory of', file_dir , 'is created')

    if (not os.path.exists(files)) or (os.path.getsize == 0):
        with open(files, 'w') as f:
            pass
        logging.info(f'creating empty file of path {files}')

    else:
        logging.info(f'{files} it already exists')
