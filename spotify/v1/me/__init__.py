from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.v1.me.album import AlbumList
from spotify.v1.me.following import FollowingList
from spotify.v1.me.player import PlayerContext
from spotify.v1.me.playlist import PlaylistList
from spotify.v1.me.top import TopContext
from spotify.v1.me.track import TrackList


class MeContext(object):

    def __init__(self, version):
        self.version = version

        self._albums = None
        self._following = None
        self._player = None
        self._playlists = None
        self._top = None
        self._tracks = None

    @property
    def albums(self):
        if not self._albums:
            self._albums = AlbumList(self.version)

        return self._albums

    @property
    def following(self):
        if not self._following:
            self._following = FollowingList(self.version)

        return self._following

    @property
    def player(self):
        if not self._player:
            self._player = PlayerContext(self.version)

        return self._player

    @property
    def playlists(self):
        if not self._playlists:
            self._playlists = PlaylistList(self.version)

        return self._playlists

    @property
    def top(self):
        if not self._top:
            self._top = TopContext(self.version)

        return self._top

    @property
    def tracks(self):
        if not self._tracks:
            self._tracks = TrackList(self.version)

        return self._tracks

    def fetch(self):
        response = self.version.request('GET', '/me')
        return MeInstance(self.version, response.json())


class MeInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties
        self._context = MeContext(self.version)

    def refresh(self):
        response = self.version.request('GET', self.href)
        self._properties = response.json()

    @property
    def birthdate(self):
        return self._properties['birthdate']

    @property
    def country(self):
        return self._properties['country']

    @property
    def display_name(self):
        return self._properties['display_name']

    @property
    def email(self):
        return self._properties['email']

    @property
    def external_urls(self):
        return self._properties['external_urls']

    @property
    def followers(self):
        return Followers.from_json(self._properties['followers'])

    @property
    def href(self):
        return self._properties['href']

    @property
    def id(self):
        return self._properties['id']

    @property
    def images(self):
        return [Image.from_json(image) for image in self._properties['image']]

    @property
    def product(self):
        return self._properties['product']

    @property
    def type(self):
        return self._properties['type']

    @property
    def uri(self):
        return self._properties['uri']

    @property
    def albums(self):
        return self._context.albums

    @property
    def following(self):
        return self._context.following

    @property
    def player(self):
        return self._context.player

    @property
    def playlists(self):
        return self._context.playlists

    @property
    def top(self):
        return self._context.top

    @property
    def tracks(self):
        return self._context.tracks
