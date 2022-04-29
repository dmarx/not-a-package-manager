# not-a-package-manager
utilities to facilitate working with codebases that don't ascribe to normal package management paradigms, e.g. ML research code that can be cloned but not installed.

**DISCLAIMER:** This tool encapsulates what could be considered "best practices" for... bad practices. Simply invoking this package should probably be considered a code smell and shouldn't come anywhere near production code.

# Installation

    pip install napm

# Usage

To "install" a codebase from a git repo:

    import napm

    url = "https://github.com/crowsonkb/cloob-training"
    napm.pseudoinstall_git_repo(url, package_name='cloob')

    import cloob

After installation, importing napm will make the "installed" packages available again

    import napm
    import cloob


# Who is this for?

If you are "installing" pacakages using code that looks something like:

    try:
        import packageName
    except:
        !git clone https://github.com/publisher/packageName
        import sys
        sys.path.append('.')

this tool is intended to replace that sort of thing.

# How it works

The tool assigns a subdirectory of the user's cache as the download location for codebases that need to be imported but can't be installed.
"Installing" then clones the target git repo into this subdirectory if it doesn't already exist. Code "installed" in this way will now be available
to any python environment into which napm is installed. 

# Why is this better?

* Replaces certain patterns that can lead to bug-prone code
* Keeps your PYTHON_PATH variable clean
* Importing tools will no longer be sensitive to or contingent on the current working directory
* Frequently reused dependencies won't need to be downloaded repeated
* You won't need to have multiple copies of the same codebase sprinkled all over your system

# Dev installation

    !pip install poetry
    !git clone https://github.com/dmarx/not-a-package-manager
    !cd not-a-package-manager; git pull origin; poetry build
    !pip uninstall -y napm; pip install not-a-package-manager/dist/napm*.whl

