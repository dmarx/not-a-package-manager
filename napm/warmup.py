from pathlib import Path
import sys

from loguru import logger

from .pseudo_install import resolve_napm_path
from .config import NapmConfig
from .update import effect_automated_updates


def populate_pythonpaths(
    env_name=None,
):
    """
    If packages have been previously "installed" with napm, this will add the "install" directories
    to the python path.
    """
    napm_paths = []
    napm_path = Path(resolve_napm_path())
    napm_paths.append(napm_path)
    if env_name:
        env_path = napm_path / env_name
        napm_paths.append(env_path)

    effect_automated_updates(env_name=env_name)
    config = NapmConfig(env_name=env_name).load()
    for package_name, package_meta in config.packages.items():
        if package_meta.add_install_dir_to_path:
            package_path = package_meta['install_dir']
            napm_paths.append(package_path)

    for path in napm_paths:
        if isinstance(path, Path):
            path = str(path.resolve())
        if path not in sys.path:
            sys.path.append(path)


if __name__ == "__main__":
    populate_pythonpaths()
