#from distutils.command import install
import importlib
from pathlib import Path
from loguru import logger
#import os
import sys


from .utils import gitclone, resolve_napm_path
from .config import NapmConfig

def make_install_dir(dirname, env_name=None) -> str:
    """
    Creates the directory into which the package will be "installed".
    """
    parent = resolve_napm_path(env_name=env_name)
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
    env_name=None,
    auto_update=False,
    ):
    """
    Clones a git repo, adds the install dir to `sys.path` if necessary, and
    then attempts to import the package
    
    :param package_url: the url of the git repo to clone
    :param install_dir: The directory where the package will be installed. If not specified, a directory
    will be created in the current working directory
    :param package_name: the name of the package you want to install
    :param add_install_dir_to_path: If the package is not found in the install dir, add the install dir
    to sys.path, defaults to False (optional)
    :param auto_update: If true, will always attempt a git pull prior to loading module
    """
    install_successful = False
    if not package_name:
        package_name = package_url.split('/')[-1]
    if not install_dir:
        install_dir = make_install_dir(package_name, env_name=env_name)
    
    gitclone(package_url, install_dir)

    # test install was successful
    try:
        importlib.import_module(package_name)
        install_successful = True
    except ImportError as e:
        logger.error(f'{package_name} failed to import from napm install dir')
        add_install_dir_to_path = True

    if add_install_dir_to_path:
        sys.path.append(install_dir)
        logger.debug(f"Added {install_dir} to sys.path")

    # validate that the package was "installed"
    try:
        importlib.import_module(package_name)
        install_successful = True
    except ImportError as e:
        logger.error(f"Failed to import {package_name}, napm 'install' failed")
        raise e
    
    if install_successful:
        config = NapmConfig(env_name=env_name)
        config.add_package(
            package_name=package_name,
            install_dir=install_dir,
            add_install_dir_to_path=add_install_dir_to_path,
            auto_update=auto_update,
        )
