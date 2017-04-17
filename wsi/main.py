import os


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
    if app.repository is None:
        for k, dir_ in SCRIPTS.items():
            module_ = _get_module(app, dir_)
    else:
        repo = app.repository
        dir_ = SCRIPTS[repo]
        module_ = _get_module(app, dir_)

    return module_


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
    for app in apps:
        m_ = find_module(app)

        if not m_:
            raise FileNotFoundError

        if is_installed(m_):
            continue
        else:
            m_.install()


def main():
    pass


if __name__ == '__main__':
    main()
