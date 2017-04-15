

class Pattern:
    def __init__(self, name=None, publisher=None, version=None):
        self.name = name
        self.publisher = publisher
        self.version = version


class App:
    def __init__(self, name, version=None, repository=None, install_options=None, settings=None):
        self.repository = repository

        self.name = name

        self.version = version

        self.install_options = install_options

        self.settings = settings
