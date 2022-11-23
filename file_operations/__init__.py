"""This file contains os file operations"""

import os


def get_current_working_directory() -> str:
    """returns current working directory"""

    return os.getcwd()


def join_path(list_of_paths: list) -> str:
    """returns the concat list"""

    return os.path.join(*list_of_paths)


def make_dir(path: str) -> None:
    """creates directory"""

    os.mkdir(path)
