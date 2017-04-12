from wsi.des import Pattern

is_app = True

IS_APP_STABLE = True

reg_pattern = {
    'DisplayName': '7-Zip 16.04',
    'Publisher': 'Igor Pavlov',
    'DisplayVersion': '16.04',
}


# def is_installed():
#    pass


_exefilename = '7z1604.exe'

SRCS = [
    {'filename': _exefilename,
     'uri':      'http://7-zip.org/a/' + _exefilename,
     'sha512':   ''}
]

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


def install(srcs):
    import os
    os.system('{} /S'.format(srcs[_exefilename]))


def config(config_option):



def uninstall(uninstall_string=None):
    import os
    os.system(uninstall_string)


<<<<<<< HEAD
def _get_installed():
    import re
    from wsi.reg_program import get_reg_apps

    _installed = []

    for one in get_reg_apps():
        if re.match('7-Zip', one.display_name):
            _installed.append(one)

    return _installed
=======
def config(settings=None):
    pass
>>>>>>> c193f92bc88887bdf61e9182a68fd92f1632c68f
