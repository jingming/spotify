

class MeContext(object):

    def __init__(self, version):
        self.version = version
        self.uri = '/me'

        self._player = None

    @property
    def player(self):
        if not self._player:
            self._player = Player()

        return self._player

    def fetch(self):
        response = self.version.request('GET', self.version.absolute_url(self.uri))
        return MeInstance(self, response)


class MeInstance(object):

    def __init__(self, context, response):
        self.context = context
