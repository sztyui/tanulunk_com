"""Configuration handling methods."""
import pathlib

import yaml


def open_config(filename: pathlib.Path):
    """Opening configuration from file."""
    with open(filename, "r", encoding="UTF-8") as stream:
        return yaml.safe_load(stream)
