from wsi import load_module

from wsi.env import is_exe, exe_dir


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


def get_scripts(world=None, repos=None, scripts=None, resources=None):
    global _world, _repos, _scripts, _resources

    _world = world
    _repos = repos
    _scripts = scripts
    _resources = resources


def get_world():
    if _world is not None:
        return _world

    elif

    if is_exe():
        pass


def get_scripts():
    pass


def get_resources():
    pass


def get_repos():
    pass

