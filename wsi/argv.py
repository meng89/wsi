import os

from wsi import load_module

from wsi.env import is_exe, exe_dir, USER_WSI_DIR


_world = None
_repos = None
_scripts = None
_resources = None


def load():
    import sys

    args = list()
    kwargs = dict()

    for _ in sys.argv[1:]:
        p_a = _.split('=', 1)
        if len(p_a) == 1:
            args.append(_)
        else:
            kwargs[p_a[0]] = p_a[1]

    save_argv(*args, **kwargs)


def save_argv(world=None, repos=None, scripts=None, resources=None):
    global _world, _repos, _scripts, _resources

    _world = world
    _repos = repos
    _scripts = scripts
    _resources = resources


def get_world():
    if _world is not None:
        return _world

    if is_exe():
        world = os.path.join(exe_dir(), 'world.py')
        if os.path.exists(world):
            return world

    world = os.path.join(USER_WSI_DIR, 'world.py')
    if os.path.exists(world):
        return world


def get_repos():
    if _repos is not None:
        return _repos

    if is_exe():
        world = os.path.join(exe_dir(), 'repos.py')
        if os.path.exists(world):
            return world

    world = os.path.join(USER_WSI_DIR, 'repos.py')
    if os.path.exists(world):
        return world


def get_scripts():
    if _scripts is not None:
        return _scripts

    return os.path.join(os.path.dirname(get_repos()), 'scripts')


def get_resources():
    if _resources is not None:
        return _resources

    return os.path.join(os.path.dirname(get_repos()), 'resources')
