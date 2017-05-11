

class Pattern:
    def __init__(self, name=None, publisher=None, version=None):
        self.name = name
        self.publisher = publisher
        self.version = version


class App:
    def __init__(self, name, version=None, repository=None, io=None, so=None):
        self.repository = repository

        self.name = name

        self.version = version

        # Installtion Options
        self.io = io

        # Software Options
        self.so = so
