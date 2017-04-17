# coding=utf-8

import winger


class RegApp:
    def __init__(self, display_name, display_version, publisher=None, uninstall_string=None, is_hidden=None):
        self.display_name = display_name
        self.display_version = display_version
        self.publisher = publisher
        self.uninstall_string = uninstall_string
        self.is_hidden = is_hidden

