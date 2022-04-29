from .warmup import populate_pythonpaths
from .pseudo_install import resolve_napm_path, pseudoinstall_git_repo

populate_pythonpaths()

__all__ = ['resolve_napm_path', 'pseudoinstall_git_repo']
