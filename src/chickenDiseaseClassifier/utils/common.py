# Import necessary libraries and modules
import os
from box.exceptions import BoxValueError
import yaml
from chickenDiseaseClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# Utility Functions for File Handling


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Exception if unable to read the file.

    Returns:
        ConfigBox: A ConfigBox object representing the content of the YAML file.
    """
    try:
        # Attempt to open and load the YAML file
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # Log success message
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            # Return content as ConfigBox
            return ConfigBox(content)
    except BoxValueError:
        # Raise an exception if the YAML file is empty
        raise ValueError("YAML file is empty")
    except Exception as e:
        # Raise an exception if unable to read the file
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories.

    Args:
        path_to_directories (list): List of paths of directories to be created.
        verbose (bool, optional): Display log messages. Defaults to True.
    """
    # Iterate through each directory path in the list
    for path in path_to_directories:
        # Create the directory if it doesn't exist, ignore if it does
        os.makedirs(path, exist_ok=True)
        # Log the creation if verbose is True
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save JSON data to a specified path.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    # Open the file and write JSON data with indentation for readability
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    # Log success message
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON files' data.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    # Open the file, load JSON data, and wrap it in ConfigBox
    with open(path) as f:
        content = json.load(f)

    # Log success message
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data to a specified path.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    # Save binary data using joblib.dump
    joblib.dump(value=data, filename=path)
    # Log success message
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary data.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Object stored in the file.
    """
    # Load binary data using joblib.load
    data = joblib.load(path)
    # Log success message
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    # Calculate size in KB and round to nearest integer
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    """
    Decode a base64-encoded image string and save it to a file.

    Args:
        imgstring (str): Base64-encoded image string.
        fileName (str): Name of the file to save the image.
    """
    # Decode base64 string and write to file
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    Encode an image file into a base64 string.

    Args:
        croppedImagePath (str): Path to the image file.

    Returns:
        str: Base64-encoded image string.
    """
    # Open the image file, read content, and encode to base64
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
