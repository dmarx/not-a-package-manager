from .pseudo_install import resolve_napm_path 
from pathlib import Path
import sys
from loguru import logger

def populate_pythonpaths():
    """
    If packages have been previously "installed" with napm, this will add the "install" directories to the python path.
    """
    napm_path = Path(resolve_napm_path())
    sys.path.append(napm_path)
    #for subdir in napm_path.iterdir():
    #    if subdir.is_dir():
    #        subdir = str(subdir.resolve())
    #        logger.debug(subdir)
    #        sys.path.append(subdir)

if __name__ == "__main__":
    populate_pythonpaths()