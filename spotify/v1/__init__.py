from spotify.v1.album import AlbumList
from spotify.v1.me import MeContext


class V1(object):

    def __init__(self, client):
        self.client = client
        self.uri = '/v1'

        self._albums = None
        self._me = None

    def absolute_url(self, uri):
        return self.client.absolute_url('{}{}'.format(self.uri, uri))

    def request(self, method, uri, params=None, data=None):
        return self.client.request(method, self.absolute_url(uri), params=params, data=data)

    @property
    def me(self):
        if not self._me:
            self._me = MeContext(self.client)

        return self._me

    @property
    def albums(self):
        if not self._albums:
            self._albums = AlbumList(self)

        return self._albums
