import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'plantDiseaseDetection'

list_of_files = [
    '.github/workflows/.gitkeep', # For github action
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/config/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/constants/__init__.py',
    f'notebook/{project_name}.ipynb',
    'config/config.yaml',
    'params.yaml',
    'setup.py',
    'requirements.txt'
]


for filepath in list_of_files:
    
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    print(filedir + "--" + filename)

    if (filedir != '') and (not os.path.exists(filedir)):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} already exists")

    
    
    