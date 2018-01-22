

class Page(object):

    def __init__(self, version, data, key):
        self.version = version

        self.items = [self.instance_class(self.version, item) for item in data[key]]

    @property
    def instance_class(self):
        raise NotImplementedError()
