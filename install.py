import importlib
import importlib.util
import os
import sys

import wsi
from wsi import load_module
from wsi.descriptions import WorldApp
from wsi.reg_program import RegApp


def read_all_patterns(repos):
    def _filter(filename):
        if filename.startswith('.py'):

    for repo, path in repos:

        for _p, _dirs, _files in os.walk(path):
            pyfiles = [one for one in _files if one.endswith('.py')]



def is_match(reg_app: RegApp, patterns: list):
    reg_app


def get_installed_apps():
    from wsi import reg_program
    for reg_app in reg_program.get_reg_apps():
        app_name = is_match(reg_app, )


def match_module(worldapp: WorldApp):

    app_dirs = []

    if worldapp.repository:
        app_dirs.append(wsi._repos[worldapp.repository] + '/' + worldapp.name)

    else:
        for repo_dir in wsi._repos.values():
            app_dirs.append(repo_dir + '/' + worldapp.name)

    app_dirs = [os.path.abspath(_d) for _d in app_dirs]


    modules = []

    for _repo_name, _repo_path in wsi._repos:
        if worldapp.repository is not None and worldapp.repository != _repo_name:
            continue

        app_dir = os.path.abspath(os.path.join(_repo_path, worldapp.name))

        if not os.path.isdir(app_dir):
            continue

        for _f in app_dir:
            pyfile = os.path.abspath(os.path.join(app_dir, _f + '.py'))

            if not os.path.isfile(pyfile):
                continue

            _module = load_module(pyfile)

            if not hasattr(_module, 'is_app') or not _module.is_app:
                continue

            if worldapp.version:
                if os.path.abspath(os.path.join(app_dir, worldapp.version + '.py')) == pyfile:
                    return _module

                elif worldapp.version in _module.versions:
                    modules.append(_module)

            elif _module.is_stable:
                modules.append(_module)

    if not modules:
        raise Exception


    ver_to_modules = {}

    for _module in modules:
        v = None

        try:
            higher = load_module(os.path.basename(_module.__file__) + '/' + '__compare_verison.py').higher
        except FileNotFoundError:
            higher = wsi.default_higher

        for _v in _module.versions:
            if v is None:
                v = _v
            elif v == _v:
                continue
            elif higher(_v, v):
                v = _v
        v =





def read_config():
    import config

    def temp(repos_or_dists, pyfile=None):
        dic = {}
        for path in repos_or_dists:
            abs_path = os.path.abspath(os.path.join(os.path.dirname(config.__file__, ), path))
            repo_or_dist = load_module(abs_path + '/' + pyfile)
            dic[repo_or_dist.name] = abs_path

        return dic

    return temp(config.repositories, '__repository.py'), temp(config.distfileses, '__distfiles.py')


def main():
    import wsi
    repos, dists = read_config()
    wsi._repos = repos
    wsi._dists = dists


    if len(sys.argv) > 1:
        profile = importlib.import_module(sys.argv[1])
    else:
        profile = importlib.import_module('world')

    all_patterns = read_all_patterns(repos)

    apps_modules = []
    for worldapp in profile.apps:
        apps_modules.append((worldapp, match_module(worldapp)))

    for worldapp, module in apps_modules:

        if not module.IS_INSTALLED():
            module.INSTALL()

        module.CONFIG(settings=worldapp.settings)

    input('\nDone, press any key to exit.\n')


if __name__ == '__main__':
    main()
