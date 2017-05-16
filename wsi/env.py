import sys
import os

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
