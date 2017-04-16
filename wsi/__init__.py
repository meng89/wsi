import importlib.util
import os

version = (0, 0, 1)

# OFFICAL_REPO_NAME = 'offical'

_repos = {}

_dists = {}


_modules = {}


def load_module(pypath, my_file=None):

    def _get_module_from_file_py35(_path):
        spec = importlib.util.spec_from_file_location(_path, _path)
        _module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_module)
        return _module

    def _get_module_from_file_py34(_path):
        from importlib.machinery import SourceFileLoader
        _module = SourceFileLoader(_path, _path).load_module()
        return _module

    _p = ''

    if my_file is not None:
        _p = os.path.dirname(my_file)

    abs_path = os.path.abspath(os.path.join(_p, pypath))

    try:
        return _modules[abs_path]
    except KeyError:
        try:
            _modules[abs_path] = _get_module_from_file_py35(abs_path)
        except AttributeError:
            _modules[abs_path] = _get_module_from_file_py34(abs_path)

        return _modules[abs_path]
