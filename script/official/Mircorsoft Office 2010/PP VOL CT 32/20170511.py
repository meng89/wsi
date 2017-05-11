
_iso = 'SW_DVD5_Office_Professional_Plus_2010_W32_ChnTrad_MLF_X16-52767.iso'
_sp2 = 'officesp2010-kb2687455-fullfile-x86-zh-tw.exe'

__sp2_sc = 'https://download.microsoft.com/download/4/7/5/47529742-9E34-4D20-BF5A-64C3C60C6299/officesp2010-kb2687455-fullfile-x86-zh-cn.exe'
SRCS = [
    {'filename': _iso,
     'uri':      'ed2k://|file|SW_DVD5_Office_Professional_Plus_2010_W32_ChnTrad_MLF_X16-52767.iso'
                 '|913917952|05C7B0C53F7A116573078176F7F09BBF|/',
     'hash':   ('sha1', 'D41BD35BD589ABF84F66D7F76CA594BA54E4E5F4')
     },

    {'filename': _sp2,
     'uri':      'https://download.microsoft.com/download/F/5/1/F51D9028-A2F8-471F-9758-BB652D84F683/'
                 'officesp2010-kb2687455-fullfile-x86-zh-tw.exe',
     'hash':  ()
     }
]

ALL_INSTALL_OPTIONS = 'ex_po_wo_ou'
INSTALL_OPTION = {}


def install(io=None):
    pass


def config(so=None):
    pass
