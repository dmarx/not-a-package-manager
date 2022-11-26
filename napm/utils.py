import os
from pathlib import Path
import subprocess
import sys
#import importlib
#import omegaconf

from loguru import logger

#from napm.config import NapmConfig
from .config import NapmConfig


# should we use an SDK for this instead? Maybe https://gitpython.readthedocs.io/en/stable/tutorial.html ?
def gitclone(
    repo_url, 
    tgt_dir,
    recurse_submodules=True
    ):
    """
    Alias for calling git clone.
    """
    #cmd = ['git', 'clone']
    #cmd += [url, tgt_dir]
    cmd = ['git', 'clone']
    if recurse_submodules:
        cmd += ['--recurse-submodules']
    cmd += [repo_url, tgt_dir]
    res = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    #logger.debug(res)


def gitupdate(
    install_dir,
):
    """
    Updates a git repo.
    """
    # https://git-scm.com/docs/git#Documentation/git.txt--Cltpathgt
    logger.debug(f'attempting to invoke git pull on {install_dir}')
    cmd = ['git','-C',install_dir, 'pull', 'origin']
    res = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')

    
def install_requirements(package_name):
    cfg = NapmConfig().load()
    root = Path(cfg.packages[package_name].install_dir)
    reqs_path = (root /'requirements.txt')
    if reqs_path.exists():
        retval = subprocess.run(
            ['pip','install','-r',str(reqs_path.resolve())]
            , stdout=subprocess.PIPE
        ).stdout.decode('utf-8')
    return retval

#install_dir = Path(__path__)
#local_path = Path.cwd() 

# to do: add a database (maybe just a text file) to track mappings from package name to install dir


#Path.expanduser()

# TO DO: check for an enviroment variable that can be used to override the install directory


def resolve_napm_path(env_name=None) -> str:
    """
    Returns the parent direectory into which napm will "install" "pacakages"
    """
    # TO DO: better internal jargon to replace scarequotes
    # Todo: after first resolve, persist this to a config file or something like that and load from there. 
    napm_path = os.environ.get('NAPM_PATH')
    if napm_path is None:
        cache_dir = Path.home() / '.cache' / 'napm' 
        if env_name:
            cache_dir = cache_dir / '_envs' / env_name
        napm_path = (cache_dir).resolve()
        napm_path.mkdir(parents=True, exist_ok=True)
    napm_path = str(napm_path)
    if napm_path not in sys.path:
        sys.path.append(napm_path)
    return napm_path
