import shutil
import pathlib

from loguru import logger

from .pseudo_install import resolve_napm_path
from .utils import resolve_napm_path
from .config import NapmConfig


def remove_package(
    package_name,
    env_name=None,
    config_path=None,
):
    """
    Updates (git pull) the specified "package" in the specified "environment".
    """
    # this chunk is lifted from update_package.py, maybe I could abstract with a decorator?
    logger.debug(package_name)
    config = NapmConfig(env_name=env_name, config_path=config_path)
    config = config.load()
    if package_name in config['packages']:
        install_dir = config['packages'][package_name]['install_dir']
        install_dir = pathlib.Path(install_dir)
        shutil.rmtree(install_dir)
        del config['packages'][package_name]
    else:
        raise ValueError("Package not found in config.")
    ### uncomment this after we add some safety checks or maybe make it optional, feels unsafe.
    #config = config.load()
    #if not config['packages']:
    #    env_dir = config.config_path.parent
    #    shutil.rmtree(env_dir)
    #else:
    #    raise Exception(
    #        "something weird happened, you should never see this. "
    #        "Please file an issue at https://github.com/dmarx/not-a-package-manager/issues/new"
    #    )


def remove_env(
    env_name=None,
    config_path=None,
):
    logger.debug(env_name)
    config = NapmConfig(env_name=env_name, config_path=config_path)
    config = config.load()
    for package in config['packages']:
        remove_package(
            package_name=package,
            env_name=env_name,
            config_path=config_path,
        )
