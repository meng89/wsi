import os
from subprocess import Popen, PIPE
import io

import chardet

from wsi.env import wincdemu_path





def mount(file):
    file = os.path.realpath(file)

    ip = Popen([wincdemu_path(), '/install'])
    ip.wait()

    mp = Popen([wincdemu_path(), file])
    _1 = 'Listing connected virtual CDs:'
    _2 = 'Letter  Image file'

    _end_line = '------------------------------'

    _b = Popen([wincdemu_path(), '/list']).communicate()[0]
    _code = chardet.detect(_b)['encoding']

    bytes_file = io.BytesIO(_b)

    lines = [line.decode(_code).rstrip() for line in bytes_file.readlines()]

    for line in lines:
