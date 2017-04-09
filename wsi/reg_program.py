# coding=utf-8

import winreg


class RegApp:
    def __init__(self, display_name, display_version, publisher=None, uninstall_string=None, is_hidden=None):
        self.display_name = display_name
        self.display_version = display_version
        self.publisher = publisher
        self.uninstall_string = uninstall_string
        self.is_hidden = is_hidden


def get_reg_apps():
    regapps = []

    for i in (r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
              r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall'):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
        for j in range(winreg.QueryInfoKey(key)[0]):
            try:
                each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                          i + '\\' + winreg.EnumKey(key, j),
                                          0,
                                          winreg.KEY_ALL_ACCESS
                                          )

                p = RegApp(display_name=winreg.QueryValueEx(each_key, 'DisplayName')[0],
                           display_version=winreg.QueryValueEx(each_key, 'DisplayVersion')[0],
                           publisher=winreg.QueryValueEx(each_key, 'Publisher')[0],
                           uninstall_string=winreg.QueryValueEx(each_key, '')
                           )
                regapps.append(p)

            except WindowsError:
                pass

    return regapps


