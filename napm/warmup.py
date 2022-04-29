from .pseudo_install import resolve_dapm_path 
from pathlib import Path
import sys
from loguru import logger

def populate_pythonpaths():
    """
    If packages have been previously "installed" with dapm, this will add the "install" directories to the python path.
    """
    dapm_path = Path(resolve_dapm_path())
    for subdir in dapm_path.iterdir():
        if subdir.is_dir():
            subdir = str(subdir.resolve())
            logger.debug(subdir)
            sys.path.append(subdir)

if __name__ == "__main__":
    populate_pythonpaths()