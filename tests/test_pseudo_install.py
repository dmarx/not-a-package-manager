from importlib import reload

import pytest

def test_pseudoinstall_git_repo_toplevel():
    import napm
    url = "https://github.com/crowsonkb/cloob-training"
    napm.pseudoinstall_git_repo(url, package_name='cloob')

    reload(napm)
    import cloob
    from cloob.cloob_training import model_pt, pretrained

def test_pseudoinstall_git_repo_subdir():
    import napm
    url = "https://github.com/facebookresearch/SLIP"
    napm.pseudoinstall_git_repo(url, add_install_dir_to_path=True)

    reload(napm)
    import SLIP
    from SLIP.models import SLIP_VITB16, SLIP, SLIP_VITL16
