import os
from subprocess import Popen
from wsi.env import wincdemu_path


def mount(file):
    p = Popen([wincdemu_path(), '/install'])
    p.wait()

    p = Popen([wincdemu_path(), ])