_exefilename = 'WinCDEmu-4.1.exe'

MAIN_SRC = {'FILENAME': _exefilename,
            'URI': 'http://sysprogs.com/files/WinCDEmu/' + _exefilename,
            'SHA512': ''}


def INSTALL(*args, **kwargs):
    import os
    from wsi import env

    os.system('{}/{} /S'.format(env.RESOURCES['official'], _exefilename))


def IS_INSTALLED():
    pass


