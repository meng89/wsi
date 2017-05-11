from wsi.des import App

sz = App(name='7-Zip', version='16.04',
         so={'cua': ['7z', 'zip', 'rar'], 'aua': ['7z', 'zip', 'rar']}
         )

office2010 = App('Microsoft Office 2010/PP VOL CT 32', version='20170511',
                 io={'features': ['word', 'excel', 'powerpoint']})

# adobe_reader = P('Adobe Reader',)


apps_only_be_depended = App(name='lib1')

apps = (sz,)
