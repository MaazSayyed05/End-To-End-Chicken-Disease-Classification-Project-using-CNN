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
        os.amkedirs(path, exist_ok=True)

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


