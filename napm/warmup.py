from pathlib import Path
import sys

from loguru import logger

from .config import NapmConfig
from .update import effect_automated_updates
from .utils import resolve_napm_path

def populate_package_pythonpaths(
    package_name,
    env_name=None,
):
    config = NapmConfig(env_name=env_name).load()
    napm_paths = [config.env_root]
    package_meta = config.packages[package_name]
    
    package_path = Path(package_meta['install_dir'])
    if package_meta.add_install_dir_to_path:
        napm_paths.append(package_path)

    target_paths = package_meta.get('target_paths', [])
    if target_paths is None:
        target_paths = []
    for p in target_paths:
        p = package_path / p
        napm_paths.append(p)

    for path in set(napm_paths):
        if isinstance(path, Path):
            path = str(path.resolve())
        if path not in sys.path:
            sys.path.append(path)

def populate_pythonpaths(
    env_name=None,
):
    """
    If packages have been previously "installed" with napm, this will add the "install" directories
    to the python path.
    """
    effect_automated_updates(env_name=env_name)
    config = NapmConfig(env_name=env_name).load()
    for package_name in config.packages:
        populate_package_pythonpaths(
            package_name=package_name,
            env_name=env_name,
        )


if __name__ == "__main__":
    populate_pythonpaths()
