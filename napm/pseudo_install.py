from distutils.command import install
import importlib
from pathlib import Path
from loguru import logger
from omegaconf import OmegaConf
import os
import sys

import importlib

from .utils import gitclone

#install_dir = Path(__path__)
#local_path = Path.cwd() 

# to do: add a database (maybe just a text file) to track mappings from package name to install dir


#Path.expanduser()

# TO DO: check for an enviroment variable that can be used to override the install directory




def resolve_napm_path() -> str:
    """
    Returns the parent direectory into which dapm will "install" "pacakages"
    """
    # TO DO: better internal jargon to replace scarequotes
    # Todo: after first resolve, persist this to a config file or something like that and load from there. 
    napm_path = os.environ.get('NAPM_PATH')
    if napm_path is None:
        cache_dir = Path.home() / '.cache'
        napm_path = (cache_dir / 'napm').resolve()
        napm_path.mkdir(parents=True, exist_ok=True)
    napm_path = str(napm_path)
    if napm_path not in sys.path:
        sys.path.append(napm_path)
    return napm_path


def make_install_dir(dirname) -> str:
    """
    Creates the directory into which the package will be "installed".
    """
    parent = resolve_napm_path()
    install_dir = Path(parent) / dirname
    if not install_dir.exists():
        install_dir.mkdir(parents=True)
    else:
        logger.warning(f'{install_dir} already exists')
    install_dir = str(install_dir)
    return install_dir


def pseudoinstall_git_repo(
    package_url, 
    install_dir=None, 
    package_name=None,
    add_install_dir_to_path=False,
    ):
    if not package_name:
        package_name = package_url.split('/')[-1]
    if not install_dir:
        install_dir = make_install_dir(package_name)
    
    gitclone(package_url, install_dir)

    # test install was successful
    try:
        importlib.import_module(package_name)
    except ImportError as e:
        logger.error(f'{package_name} failed to import from dapm install dir')
        add_install_dir_to_path = True

    if add_install_dir_to_path:
        sys.path.append(install_dir)
        logger.debug(f"Added {install_dir} to sys.path")

    try:
        importlib.import_module(package_name)
    except ImportError as e:
        logger.error(f"Failed to import {package_name}, napm 'install' failed")
        raise e
