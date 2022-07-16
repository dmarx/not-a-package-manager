import importlib
import loguru
import pytest
import sys

from napm.remove import (
    remove_package,
    remove_env,
)


# tmp_path fixture won't work here.
# for time being, I could reserve an env name for testing
#def test_remove_package(tmp_path):
def test_remove_package():
    import napm
    url = "https://github.com/dmarx/napm_test"
    #napm.pseudoinstall_git_repo(url, env_name='tmp', install_dir=tmp_path)
    napm.pseudoinstall_git_repo(url, package_name='TO_BE_REMOVED', env_name='_temp_test_reserved')
    napm.populate_pythonpaths(env_name='_temp_test_reserved') # hmm... I don't think this will work, right?
    import TO_BE_REMOVED
    remove_package(package_name='TO_BE_REMOVED', env_name='_temp_test_reserved')

    outcome = False
    try:
        #import TO_BE_REMOVED # pseudoinstall loads the package, I need to do a reload operation
        # importlib.import_module(package_name)
        #importlib.reload('TO_BE_REMOVED')
        importlib.reload(TO_BE_REMOVED)
        assert False
    except ImportError:
        outcome = True

    assert outcome


def test_remove_env():
    assert True
