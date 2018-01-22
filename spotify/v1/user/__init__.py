from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.v1.user.playlist import PlaylistList


class UserList(object):

    def __init__(self, version):
        self.version = version

    def get(self, id):
        return UserContext(self.version, id)


class UserContext(object):

    def __init__(self, version, id):
        self.version = version
        self.id = id

        self._playlists = None

    def fetch(self):
        response = self.version.request('GET', '/users/{}'.format(self.id))
        return UserInstance(self.version, response.json())

    @property
    def playlists(self):
        if not self._playlists:
            self._playlists = PlaylistList(self.version, self.id)

        return self._playlists


class UserInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties
        self._context = UserContext(self.version, self.id)

    @property
    def display_name(self):
        return self._properties['display_name']

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
        return [Image.from_json(image) for image in self._properties['images']]

    @property
    def type(self):
        return self._properties['type']

    @property
    def uri(self):
        return self._properties['uri']
