from loguru import logger

from .pseudo_install import resolve_napm_path, pseudoinstall_git_repo
from .utils import gitclone, gitupdate, resolve_napm_path
from .config import NapmConfig


def set_autoupdate_flag(
    package_name,
    env_name=None,
    value=True,
):
    """
    Sets the "automated_update" flag for the specified "package" in the specified "environment".
    """
    config = NapmConfig(env_name=env_name).load()
    if package_name in config.get('packages'):
        config['packages'][package_name]['automated_update'] = value
        config.update_config(config)
    else:
        raise ValueError("Package not found in config.")


def update_package(
    package,
    env_name=None,
    config_path=None,
    force=False,
):
    """
    Updates (git pull) the specified "package" in the specified "environment".
    """
    logger.debug(package)
    if force:
        raise NotImplementedError
    config = NapmConfig(env_name=env_name, config_path=config_path)
    config = config.load()
    if package in config['packages']:
        install_dir = config['packages'][package]['install_dir']
        gitupdate(install_dir)
    else:
        raise ValueError("Package not found in config.")


def effect_automated_updates(
    env_name=None,
):
    """
    If packages have been previously "installed" with napm and flagged for automated update, 
    this will "update" the "packages" by attempting a git pull.
    """
    config = NapmConfig(env_name=env_name).load()
    for package_name, package_meta in config.packages.items():
        if package_meta.get('automated_update'):
            update_package(package_name, env_name=env_name)


def update_environment(
    env_name=None,
    ):
    """
    Updates all "packages" that have been "installed" into the specified "environment".
    """
    config = NapmConfig(env_name=env_name).load()
    for package_name, package_meta in config.packages.items():
        update_package(package_name, env_name=env_name)
