import os
import yaml
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {path_to_yaml}") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Error reading YAML file: {path_to_yaml}") from e
    

def create_directories(path_to_dirs: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_dirs (list): List of directory paths to create.
        verbose (bool): If True, prints the created directories.

    Returns:
        None
    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"Created directory: {path}")

def save_json(path_to_json: Path, data: Any) -> None:
    """
    Saves data to a JSON file.

    Args:
        path_to_json (Path): Path to the JSON file.
        data (Any): Data to save.

    Returns:
        None
    """
    try:
        with open(path_to_json, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        raise IOError(f"Error writing to JSON file: {path_to_json}") from e