# not-a-package-manager
utilities to facilitate working with codebases that don't ascribe to normal package management paradigms, e.g. ML research code that can be cloned but not installed.

# Installation

This will be pushed to PyPI when it's... "ready". For the time being:

    !pip install poetry
    !git clone https://github.com/dmarx/not-a-package-manager
    !cd not-a-package-manager; git pull origin; poetry build
    !pip uninstall -y napm; pip install not-a-package-manager/dist/napm*.whl

# Usage

    url = "https://github.com/crowsonkb/cloob-training"
    napm.pseudoinstall_git_repo(url, package_name='cloob')

    import cloob