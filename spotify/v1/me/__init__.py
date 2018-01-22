from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.v1.me.player import PlayerContext


class MeContext(object):

    def __init__(self, version):
        self.version = version

        self._player = None

    @property
    def player(self):
        if not self._player:
            self._player = PlayerContext(self.version)

        return self._player

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
    def player(self):
        return self._context.player
