from wsi.descriptions import WorldApp

sz = WorldApp(name='7-Zip', version='16.04', settings={'cur_user_associations': ('7z', 'zip', 'rar'),
                                                       'all_users_associations': ('7z', 'zip', 'rar')})

# office2007 = P('Microsoft Office 2007 CN', features=['word', 'excel', 'powerpoint'])

# adobe_reader = P('Adobe Reader',)


apps_only_be_depended = WorldApp(name='lib1')

apps = sz,
