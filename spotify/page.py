from spotify.resource import Resource


class Page(Resource):

    def __init__(self, version, data, key):
        super(Page, self).__init__(version)
        self.items = [self.instance_class(self.version, item) for item in data.get(key, [])]

    @property
    def instance_class(self):
        raise NotImplementedError()
