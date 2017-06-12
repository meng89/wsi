import os

LOGS_DIR = os.path.join(os.getenv('LOCALAPPDATA'), 'wpi_logs')
SCRIPTS_DIR_NAME = 'scripts'
RESOURCES_DIR_NAME = 'resources'

def get_version_filenames(dirname):
    filenames = []

    for name in os.listdir(dirname):
        if name.startswith('.') or name.startswith('_'):
            continue
        if os.path.isfile(os.path.join(dirname, name)) and os.path.splitext(name)[1].lower() == '.py':
            filenames.append(name)

    return filenames


def load_modules(dir_, names):
    from wsi import load_module

    modules = []
    for _ in names:
        modules.append(load_module(os.path.join(dir_, _)))
    return modules


def filter_stable(modules):
    stables = []
    for module_ in modules:
        if getattr(module_, 'is_stable', False):
            stables.append(module_)
    return stables


def sorted_by_newest(modules, cmp=None):
    cmp = cmp or None

    return sorted(modules, key=cmp)


def _get_module(app, dir_):
    from wsi import load_module

    module_ = None

    if app.version:
        try:
            module_ = load_module(os.path.join(dir_, app.name, app.version))
        except Exception:
            pass
    else:
        filenames = get_version_filenames(dir_)
        if filenames:
            modules = load_modules(dir_, filenames)
            stables = filter_stable(modules)
            if stables:
                module_ = stables[0]
            else:
                try:
                    _m = load_module(os.path.join(dir_, '_.py'))
                    cmp_fun = getattr(_m, 'cmp_fun')
                except Exception:
                    cmp_fun = None

                sorted_modules = sorted_by_newest(modules, cmp_fun)
                module_ = sorted_modules[0]

    return module_


def find_module(app):

    from wsi.env import exe_dir, SCRIPTS

    module_ = None
    repo = None

    if app.repository is None:
        for k, dir_ in SCRIPTS.items():
            module_ = _get_module(app, dir_)
            repo = app.repository
    else:
        repo = app.repository
        dir_ = SCRIPTS[repo]
        module_ = _get_module(app, dir_)

    return module_, repo


def get_reg_apps():
    import winger

    regapps = []
    for key in (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'):
        regapps.extend(winger.Tips(key).items())
    return regapps


def is_installed(module_):
    if hasattr(module_, 'is_installed'):
        if module_.is_installed():
            return True
        else:
            return False

    else:
        regapps = get_reg_apps()

        for one in regapps:
            if one >= module_.reg_pattern:
                return True

        return False


def install(apps):
    from wsi.env import RESOURCES
    for app in apps:
        m_, repo = find_module(app)

        if not m_:
            raise FileNotFoundError

        if is_installed(m_):
            continue
        else:
            m_.install(io=app.io, resource_dir=RESOURCES[repo][app.name])


def main():
    import sys
    import ctypes
    import datetime
    import tempfile

    from wsi.env import is_exe
    from wsi.log import set_file_handler, set_stream_handler

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('Not run as Administrator!')
        sys.exit()

    args = list()
    kwargs = dict()

    for _ in sys.argv[1:]:
        p_a = _.split('=', 1)
        if len(p_a) == 1:
            args.append(_)
        else:
            kwargs[p_a[0]] = p_a[1]

    log_filename = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S_%f') + '.log.txt'
    os.makedirs(LOGS_DIR, exist_ok=True)

    set_file_handler(os.path.join(LOGS_DIR, log_filename))
    set_stream_handler()

    log_sys_info()

    os.chdir(tempfile.gettempdir())

    if is_exe():
        exe_main(*args, **kwargs)
    else:
        script_main(*args, **kwargs)


def exe_main(world=None, scripts=None, resources=None):
    import json

    from wsi.env import exe_dir

    scripts = scripts or os.path.join(exe_dir, SCRIPTS_DIR_NAME)

    resources = resources or os.path.join(exe_dir(), RESOURCES_DIR_NAME)

    repos = json.loads(open(os.path.join(exe_dir(), 'repos.josn')).read())

    for one in repos:
        if 'localtion' not in repos.keys():
            scripts = 
        elif os.path.isabs(repos['localtion']):
    install()


def script_main(world=None, scripts=None, resources=None):
    pass


def log_sys_info():
    import sys
    import logging
    from wsi.env import CUR_BIT, CUR_OS, PYTHON_BIT

    logging.info('OS bit: {}'.format(CUR_BIT))
    logging.info('OS release: {}'.format(CUR_OS))
    logging.info('Python bit: {}'.format(PYTHON_BIT))
    logging.info('Python sys.version: {}'.format(sys.version))


if __name__ == '__main__':
    main()
