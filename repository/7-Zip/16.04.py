from wsi.descriptions import Pattern

is_app = True

IS_APP_STABLE = True

patterns = (
    Pattern(name='^7-Zip', publisher='^Igor Pavlov', version='^16.04')
)


_exefilename = '7z1604.exe'

MAIN_SRC = {'FILENAME': _exefilename,
            'URI':      'http://7-zip.org/a/' + _exefilename,
            'SHA512':   ''}

INSTALL_OPTION = {}


CONFIG_OPTION = {
    'user_associations': ''
}

avl_install_options = {}
def_install_options = None

_able_associations = {'7z', 'zip', 'rar', '001', 'cab', 'iso', 'xz', 'txz', 'lzma', 'tar', 'cpio', 'bz2', 'bzip2',
                      'tbz2', 'tbz', 'gz', 'gzip', 'tgz', 'tpz', 'z', 'taz', 'lzh', 'lha', 'rpm', 'deb', 'arj', 'vhd',
                      'wim', 'swm', 'fat', 'ntfs', 'dmg', 'hfs', 'xar', 'squashfs'}
avl_settings_options = {
    'cur_user_associations': _able_associations,
    'all_users_associations': _able_associations
}
def_settings_options = None


depend = None


def install(*args, **kwargs):
    import os
    os.system('{}/{} /S'.format(kwargs['distfiles'], _exefilename))


def uninstall():
    import os
    for one in _get_installed():
        os.system(one.uninstall_cmd + '/S')


def is_installed():
    return bool(_get_installed())


def config(options):
    pass


def _get_installed():
    import re
    from wsi.reg_program import get_reg_apps

    _installed = []

    for one in get_reg_apps():
        if re.match('7-Zip', one.display_name):
            _installed.append(one)

    return _installed
