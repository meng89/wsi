import sys
import os
import platform

from collections import OrderedDict

OFFICIAL_NAME = 'official'


DEF_SCRIPT_DIRNAME = 'script'
DEF_RESOURCE_DIRNAME = 'resource'


BUNDLE_DATA_FOLDER = '_data'

WINCDEMU_NAME = 'PortableWinCDEmu-4.0.exe'


def is_exe():
    if getattr(sys, 'frozen', False) is not False:
        return True
    else:
        return False


def meipass_path():
    return getattr(sys, '_MEIPASS')


def exe_path():
    if is_exe():
        return sys.executable
    elif __file__:
        return __file__


def exe_dir():
    return os.path.dirname(exe_path())


def wincdemu_path():
    if is_exe():
        return os.path.join(meipass_path(), BUNDLE_DATA_FOLDER, WINCDEMU_NAME)


SCRIPTS = OrderedDict()

RESOURCES = OrderedDict()


class Env:
    def __init__(self):
        self.name = None
        self.version = None
        self.resource = None


CUR_OS = platform.release().lower()


if platform.machine().endswith('64'):
    CUR_BIT = '64'
elif platform.machine().endswith('86'):
    CUR_BIT = '32'
else:
    raise Exception


PYTHON_BIT = platform.architecture()[0][0:2]

USER_WSI_DIR = os.path.join(os.getenv('LOCALAPPDATA'), 'wsi')
