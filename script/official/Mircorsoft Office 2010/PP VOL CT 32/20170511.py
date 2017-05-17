
_iso = 'SW_DVD5_Office_Professional_Plus_2010_W32_ChnTrad_MLF_X16-52767.iso'
_sp2 = 'officesp2010-kb2687455-fullfile-x86-zh-tw.exe'

__sp2_sc = 'https://download.microsoft.com/download/4/7/5/47529742-9E34-4D20-BF5A-64C3C60C6299/officesp2010-kb2687455-fullfile-x86-zh-cn.exe'


def sources():
    _ = [
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
    return _

ALL_INSTALL_OPTIONS = ['Access', 'Excel', 'InfoPath', 'OneNote', 'Outlook', 'PowerPoint', 'Publisher',
                       'SharePoint Workspace', 'Visio Viewer', 'Word',
                       'Shared', 'Tools']

def_install_options = ['Excel', 'Word', 'Outlook', 'PowerPoint', 'Shared', 'Tools']


def _make_config(io):

    _ = {
        'Access': 'ACCESSFiles',
        'Excel': 'EXCELFiles',
        'InfoPath': 'XDOCSFiles',
        'OneNote': 'OneNoteFiles',
        'Outlook': 'OUTLOOKFiles',
        'PowerPoint': 'PPTFiles',
        'Publisher': 'PubPrimary',
        'SharePoint Workspace': 'GrooveFiles',
        'Visio Viewer': '',
        'Word': 'WORDFiles',
        'Shared': 'SHAREDFiles',
        'Tools': 'TOOLSFiles'
         }

    io_set = set(io)

    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, 'Configuration', None)
    root = dom.documentElement
    root.setAttribute('Product', 'ProPlus')

    display = dom.createElement('Display')
    display.setAttribute('Level', 'full')
    display.setAttribute('CompletionNotice', 'yes')
    display.setAttribute('SuppressModal', 'no')
    display.setAttribute('AcceptEula', 'yes')
    root.appendChild(display)

    for one in io_set:
        os = dom.createElement('OptionState')
        os.setAttribute('Id', _[one])
        os.setAttribute('State', 'Local')
        os.setAttribute('Children', 'Force')
        root.appendChild(os)

    return root.toprettyxml()


def install(io=None, source_files=None, env=None):
    io = io or def_install_options

    from wsi.mount import mount
    driver = mount(source_files[_iso])
    

def config(so=None):
    pass
