from spotify.v1.album import AlbumList
from spotify.v1.artist import ArtistList
from spotify.v1.me import MeContext
from spotify.v1.search import SearchContext
from spotify.v1.track import TrackList
from spotify.v1.user import UserList


class V1(object):

    def __init__(self, client):
        self.client = client
        self.uri = '/v1'

        self._albums = None
        self._artists = None
        self._me = None
        self._search = None
        self._tracks = None
        self._users = None

    def absolute_url(self, uri):
        return self.client.absolute_url('{}{}'.format(self.uri, uri))

    def request(self, method, uri, params=None, data=None, headers=None):
        return self.client.request(method, self.absolute_url(uri), params=params, data=data, headers=headers)

    @property
    def albums(self):
        if not self._albums:
            self._albums = AlbumList(self)

        return self._albums

    @property
    def artists(self):
        if not self._artists:
            self._artists = ArtistList(self)

        return self._artists

    @property
    def me(self):
        if not self._me:
            self._me = MeContext(self)

        return self._me

    @property
    def search(self):
        if not self._search:
            self._search = SearchContext(self)

        return self._search

    @property
    def tracks(self):
        if not self._tracks:
            self._tracks = TrackList(self)

        return self._tracks

    @property
    def users(self):
        if not self._users:
            self._users = UserList(self)

        return self._users
