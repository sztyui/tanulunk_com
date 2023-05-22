"""Configuration handling methods."""
import pathlib

import yaml


def to_path(filename: str | pathlib.Path) -> pathlib.Path:
    """Checks if the input is string or pathlib.Path and converts
    accordingly to the neccesary type."""
    if not isinstance(filename, pathlib.Path):
        return pathlib.Path(filename)
    return filename


def open_config(filename: str | pathlib.Path):
    """Opening configuration from file."""
    fn_path = to_path(filename)
    return yaml.safe_load(fn_path.read_text(encoding="UTF-8"))


if __name__ == "__main__":
    open_config("./config.yml")
