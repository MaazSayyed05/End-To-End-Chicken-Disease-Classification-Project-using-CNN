import os
from pathlib import Path

from ensure import ensure_annotations

from box.exceptions import BoxValueError
from chicken_disease_classification import logger

import yaml
import json
import joblib

from box import ConfigBox

from typing import Any

import base64

from kaggle.api.kaggle_api_extended import KaggleApi
import subprocess

from chicken_disease_classification import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object.

    Parameters:
    path_to_yaml : Path

    Returns:
    ConfigBox

    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty.")

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates list of directories

    Arguments: path_to_directories

    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Created Directory at {path}.")


@ensure_annotations
def save_json(path: Path, data: dict): ## to store training history data (pandas DataFrame)
    """
    save json data

    Args:
    path(Path): path to save json
    data(dict): data to be save to json file

    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}.")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())




# @ensure_annotations

# def download_kaggle_dataset(dataset_name, output_folder, kaggle_username, kaggle_key):
#     """
#     Download a Kaggle dataset and save it to a local folder if it doesn't exist.

#     Parameters:
#     - dataset_name: Name of the Kaggle dataset (e.g., 'username/dataset-name')
#     - output_folder: Path to the local folder where the dataset will be saved
#     - kaggle_username: Your Kaggle username
#     - kaggle_key: Your Kaggle API key
#     """
#     # Set Kaggle API credentials
#     api = KaggleApi()
#     # api.authenticate(username=kaggle_username, key=kaggle_key)

#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
#     print("Creating output folder")
#     # Check if the dataset already exists in the output folder
#     dataset_path = os.path.join(output_folder, dataset_name.split("/")[-1])
#     if os.path.exists(dataset_path):
#         logger.info(f"Dataset already exists in: {dataset_path}")
#         # print("")
#         return

#     print("Downloading dataset")
#     # Download the dataset
#     api.dataset_download_files(dataset_name, path=dataset_path, unzip=True)
#     # logger.info(f"Dataset downloaded and saved to: {dataset_path}")


@ensure_annotations
def download_kaggle_dataset(username, dataset_name, output_path):
    """
    Download a Kaggle dataset using the Kaggle API command.

    Parameters:
    - username: Kaggle username
    - dataset_name: Name of the Kaggle dataset
    - output_path: Local path to save the downloaded dataset (default is current directory)
    """
    # Construct the Kaggle API command
    command = f'!kaggle datasets download -d {username}/{dataset_name}t -p {output_path}'


    try:
        # Run the command in the terminal
        subprocess.run(command, shell=True, check=True)
        print(f"Dataset downloaded successfully to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

