

class Page(object):
    INSTANCE_CLASS = None

    def __init__(self, version, data, key):
        self.version = version

        self.items = [self.INSTANCE_CLASS(item) for item in data[key]]