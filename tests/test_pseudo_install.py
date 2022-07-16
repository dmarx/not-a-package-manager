from importlib import reload

import pytest


def test_pseudoinstall_git_repo_vanilla():
    import napm
    url = "https://github.com/dmarx/napm_test"

    napm.pseudoinstall_git_repo(url)

    import napm_test
    import napm_test.subdir_bar
    import napm_test.subdir_bar.module_bar
    from napm_test.subdir_bar.module_bar import bar
    import napm_test.module_foo
    from napm_test.module_foo import foo
    #from napm_test.module_foobar import foobar

    foo()
    bar()


def test_pseudoinstall_git_repo_package_name():
    import napm
    url = "https://github.com/dmarx/napm_test"
    napm.pseudoinstall_git_repo(url, package_name='TEST_AGAIN')

    import TEST_AGAIN
    import TEST_AGAIN.subdir_bar
    import TEST_AGAIN.subdir_bar.module_bar
    from TEST_AGAIN.subdir_bar.module_bar import bar
    import TEST_AGAIN.module_foo
    from TEST_AGAIN.module_foo import foo
    from TEST_AGAIN.module_foobar import foobar

    foo()
    bar()
    #foobar()


def test_pseudoinstall_git_repo_subdir():
    import napm
    url = "https://github.com/dmarx/napm_test"
    napm.pseudoinstall_git_repo(url, package_name='TEST_MORE', add_install_dir_to_path=True)
    #napm.populate_pythonpaths()

    import TEST_MORE
    import TEST_MORE.subdir_bar
    import TEST_MORE.subdir_bar.module_bar
    from TEST_MORE.subdir_bar.module_bar import bar
    import TEST_MORE.module_foo
    from TEST_MORE.module_foo import foo
    from TEST_MORE.module_foobar import foobar

    foobar() # works!


#def test_pseudo_install_into_env():
#    import napm
#    url = "https://github.com/dmarx/napm_test"
#    napm.pseudoinstall_git_repo(url, env_name="multilingual_clip", add_install_dir_to_path=True)
#    napm.populate_pythonpaths(env_name="multilingual_clip")
#    import src
#    from src import multilingual_clip
#    #text_model = multilingual_clip.load_model('M-BERT-Distil-40')

def test_pseudo_install_into_env():
    import napm
    url = "https://github.com/dmarx/napm_test"
    napm.pseudoinstall_git_repo(url, env_name='test_env')
    napm.populate_pythonpaths(env_name="test_env")
    import napm_test
