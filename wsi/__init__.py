import importlib.util
import os

version = (0, 0, 1)

# OFFICAL_REPO_NAME = 'offical'

_modules = {}

_repos = {}

_dists = {}


def load_module(pypath: str, my_file=None, repo=None):

    def _get_module_from_file(_path):
        spec = importlib.util.spec_from_file_location(_path, _path)
        _module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_module)
        return _module

    _p = ''

    if my_file is not None:
        _p = os.path.dirname(my_file)
    elif repo is not None:
        _p = _repos[repo]

    abs_path = os.path.abspath(os.path.join(_p, pypath))

    try:
        return _modules[abs_path]
    except KeyError:
        _modules[abs_path] = _get_module_from_file(abs_path)
        return _modules[abs_path]