import subprocess
#import os
#import sys
#import importlib
#import omegaconf

from loguru import logger

# should we use an SDK for this instead? Maybe https://gitpython.readthedocs.io/en/stable/tutorial.html ?
def gitclone(
    repo_url, 
    tgt_dir,
    ):
    """
    Alias for calling git clone.
    """
    #cmd = ['git', 'clone']
    #cmd += [url, tgt_dir]
    cmd = ['git', 'clone', repo_url, tgt_dir]
    res = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8')
    logger.debug(res)

