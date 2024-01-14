import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")

project_name = "chicken_disease_classification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "main.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "requirements.txt",
    "DockerFile",
    "research/trials.ipynb",
    "test.py",
    "setup.py",
    "dvc.yaml",  #### MLOPs
]

for file_path in list_of_files:
    file_path = Path(file_path)

    file_dir, file_name = os.path.split(file_path)

    # Create directory
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}.")

    # Create empty file
    if not os.path.exists(file_path) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}.")
        
    else:
        logging.info(f"File already exists: {file_path}.")

