import os

from wsi import load_module

from wsi.env import is_exe, exe_dir, USER_WSI_DIR


_world = None
_repos = None
_scripts = None
_resources = None
_conf_moulde = None


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


def save_argv(world=None, repos=None, scripts=None, resources=None, conf=None):
    global _world, _repos, _scripts, _resources, _conf_moulde

    _world = world
    _repos = repos
    _scripts = scripts
    _resources = resources

    if conf:
        _conf_moulde = load_module(conf)
        return

    if is_exe() and os.path.exists(os.path.join(exe_dir(), 'conf.py')):
        _conf_moulde = load_module(os.path.join(exe_dir(), 'conf.py'))
        return

    if os.path.exists(os.path.join(USER_WSI_DIR, 'conf.py')):
        _conf_moulde = load_module(os.path.join(USER_WSI_DIR, 'conf.py'))
        return


def get_world():
    if _world is not None:
        return _world

    if _conf_moulde and hasattr(_conf_moulde, 'world'):
        return getattr(_conf_moulde, 'world')

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

    if _conf_moulde and hasattr(_conf_moulde, 'repos'):
        return getattr(_conf_moulde, 'repos')

    if is_exe():
        world = os.path.join(exe_dir(), 'repos.py')
        if os.path.exists(world):
            return world

    world = os.path.join(USER_WSI_DIR, 'repos.py')
    if os.path.exists(world):
        return world


def get_dire(dire):

    if get_repos():
        return os.path.join(os.path.dirname(get_repos()), dire)

    if is_exe():
        return os.path.join(os.path.join(exe_dir(), dire))

    return os.path.join(os.path.join(USER_WSI_DIR, dire))


def get_scripts():
    if _scripts is not None:
        return _scripts

    return get_dire('scripts')


def get_resources():
    if _resources is not None:
        return _resources
    return get_dire('resources')
