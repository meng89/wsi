import os
from collections import OrderedDict

from wsi.env import is_exe, exe_dir


_repos = OrderedDict()

_scripts = None
_resources = None

_kscripts = 'scripts'
_kresources = 'resources'


def load(repos_file=None, scripts=None, resources=None):
    import os
    import json

    global _repos

    if repos_file:
        pass  # todo

    else:
        if is_exe():
            _repos = json.loads(open(os.path.join(exe_dir(), 'repos.josn')).read(), object_pairs_hook=OrderedDict)
        else:
            pass  # todo


def get_scripts_uri(repo_name):
    return _repos[repo_name][_kscripts]['uri']


def get_resources_uri(repo_name):
    return _repos[repo_name][_kresources]['uri']


def get_scripts_location(repo_name):
    return _get_x_location(repo_name, _kscripts)


def get_resources_location(repo_name):
    return _get_x_location(repo_name, _kresources)


def _get_x_location(repo_name, x):
    if os.path.isabs(_repos[repo_name][x]['location']):
        return _repos[repo_name][x]['location']
    else:
        if x == _kscripts and _scripts is not None:
            return os.path.join(_scripts, _repos[repo_name][x]['location'])

        elif x == _kresources and _kresources is not None:
            return os.path.join(_resources, _repos[repo_name][x]['location'])

        elif is_exe():
            return os.path.join(exe_dir(), x, _repos[repo_name][x]['location'])

        else:
            pass  # todo
