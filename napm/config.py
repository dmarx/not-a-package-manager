from pathlib import Path

from loguru import logger
from omegaconf import OmegaConf

from .utils import resolve_napm_path


class NapmConfig:
    def __init__(
        self,
        env_name=None,
        config_path=None,
    ):
        self.env_name = env_name
        self._config_path = config_path


    @property
    def config_path(
        self
    ):
        """
        Returns the path to the config file.
        """
        if not self._config_path:
            self._config_path = Path(resolve_napm_path(self.env_name)) / 'config.yaml'
        logger.debug(f'{self._config_path}')
        if not Path(self._config_path).exists():
            #Path(self._config_path).touch()
            logger.debug(f'Creating config file at {self._config_path}')
            cfg = OmegaConf.create({'packages': {}})
            OmegaConf.save(cfg, self._config_path)
        return self._config_path


    def load(
        self
    ):
        """
        Loads the config file and returns a config object.
        """
        return OmegaConf.load(self.config_path)


    def update_config(
        self,
        config,
    ):
        """
        Updates the config file with the given config object.
        """
        OmegaConf.save(config, self.config_path)


    def add_package(
        self, 
        package_name, 
        install_dir,
        add_install_dir_to_path=False,
        auto_update=False,
    ):
        """
        Adds a package to the config file.
        """
        config = self.load()
        config.packages[package_name] = {
            'install_dir': install_dir, 
            'add_install_dir_to_path': add_install_dir_to_path,
            'automated_update': auto_update,
            }
        #config.packages[package_name]['install_dir'] = install_dir
        self.update_config(config)
