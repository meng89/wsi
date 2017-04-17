# coding=utf-8

import winger


class RegApp:
    def __init__(self, display_name, display_version, publisher=None, uninstall_string=None, is_hidden=None):
        self.display_name = display_name
        self.display_version = display_version
        self.publisher = publisher
        self.uninstall_string = uninstall_string
        self.is_hidden = is_hidden


def get_reg_apps():
    regapps = []
    for key in (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'):
        regapps.extend(winger.Tips(key).items())
    return regapps


