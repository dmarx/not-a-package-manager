from .warmup import populate_pythonpaths
from .pseudo_install import resolve_napm_path, pseudoinstall_git_repo
from .remove import remove_env, remove_package
from .update import set_autoupdate_flag, update_package

populate_pythonpaths()

__all__ = [
    'resolve_napm_path',
    'pseudoinstall_git_repo',
    'remove_package',
    'remove_env',
    'set_autoupdate_flag',
    'update_package',
]
