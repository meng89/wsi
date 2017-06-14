import os
from collections import OrderedDict

from wsi.env import is_exe, exe_dir


_repos = OrderedDict()


def load(repos_file=None):
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
    return _repos[repo_name]['scripts']['uri']


def get_resources_uri(repo_name):
    return _repos[repo_name]['resources']['uri']


def get_scripts_location(repo_name):
    return _get_x_location(repo_name, 'scripts')


def get_resources_location(repo_name):
    return _get_x_location(repo_name, 'resouces')


def _get_x_location(repo_name, x):
    if os.path.isabs(_repos[repo_name][x]['location']):
        return _repos[repo_name][x]['location']
    else:
        if is_exe():
            return os.path.join(exe_dir(), x, _repos[repo_name][x]['location'])
        else:
            pass  # todo
