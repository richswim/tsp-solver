from pathlib import Path


def get_project_root():
    """
    Returns project's root folder
    """
    return Path(__file__).parent.parent
