import os
from subprocess import Popen, PIPE
import io

import chardet

from wsi.env import wincdemu_path





def mount(file):
    file = os.path.realpath(file)

    ip = Popen([wincdemu_path(), '/install'])
    ip.wait()

    Popen([wincdemu_path(), file]).communicate()

    # _l1 = 'Listing connected virtual CDs:'
    _l2 = 'Letter  Image file'

    _l3 = '------------------------------'

    _b = Popen([wincdemu_path(), '/list'], stdout=PIPE).communicate()[0]
    _code = chardet.detect(_b)['encoding']

    bytes_file = io.BytesIO(_b)

    lines = [line.decode(_code).rstrip() for line in bytes_file.readlines()]

    is_start = False

    for line in lines:
        if line.strip() == _l2:
            is_start = True
            continue
        elif line.strip() == _l3:
            break

        if is_start:
            drive, _ = line.split(' ', 1)
            mounted_file = _.strip()
            if file == mounted_file:
                return drive

    return None


def unmount(file):
    Popen([wincdemu_path(), '/umount', file])