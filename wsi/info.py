

BIT32 = 1
BIT64 = 2


def bit():
    import platform

    if platform.architecture()[0] == '32bit':
        return BIT32
    elif platform.architecture()[0] == '64bit':
        return BIT64
    else:
        raise Exception(platform.architecture()[0])


def lang():
    import locale

    return locale.getdefaultlocale()[0]
