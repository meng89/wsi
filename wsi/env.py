import sys
import os

from collections import OrderedDict

OFFICIAL_NAME = 'official'


DEF_SCRIPT_DIRNAME = 'script'
DEF_RESOURCE_DIRNAME = 'resource'


BUNDLE_DATA_FOLDER = '_data'


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


SCRIPTS = OrderedDict()

RESOURCES = OrderedDict()


class Env:
    def __init__(self):
        self.name = None
        self.version = None
        self.resource = None
