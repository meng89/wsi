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
     'sha256':   ''}
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


def depend():
    return None


def against():
    return None


def install(resource_dir):
    import os
    os.system('{} /S'.format(os.path.join(resource_dir, _exefilename)))


def uninstall(uninstall_string=None):
    import os
    os.system(uninstall_string)


def config(settings=None):
    pass
