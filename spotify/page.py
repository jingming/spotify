from spotify.resource import Resource


class Page(Resource):

    def __init__(self, version, data, key):
        super(Page, self).__init__(version)

        self._key = key
        self._items = iter([self.instance_class(self.version, item) for item in data.get(key, [])])

        del data[key]
        self._meta = data

    def __iter__(self):
        return self._items

    def __next__(self):
        return next(self._items)

    def has_next_page(self):
        return 'next' in self._meta and self._meta['next'] is not None

    def next_page(self):
        response = self.version.request(self._meta['next'])

        return self.__class__(
            self.version,
            response.json(),
            self._key
        )

    @property
    def instance_class(self):
        raise NotImplementedError()
