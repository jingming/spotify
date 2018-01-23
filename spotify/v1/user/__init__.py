from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.resource import Instance, Resource
from spotify.v1.user.playlist import PlaylistList


class UserList(Resource):

    def get(self, id):
        return UserContext(self.version, id)


class UserContext(Resource):

    def __init__(self, version, id):
        super(UserContext, self).__init__(version)
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


class UserInstance(Instance):

    def __init__(self, version, properties):
        super(UserInstance, self).__init__(version, properties)
        self._context = UserContext(self.version, self.id)

    @property
    def display_name(self):
        return self.property('display_name')

    @property
    def external_urls(self):
        return self.property('external_urls')

    @property
    def followers(self):
        return Followers.from_json(self.property('followers'))

    @property
    def href(self):
        return self.property('href')

    @property
    def id(self):
        return self.property('id')

    @property
    def images(self):
        return [Image.from_json(image) for image in self.property('images')]

    @property
    def type(self):
        return self.property('type')

    @property
    def uri(self):
        return self.property('uri')

    @property
    def playlists(self):
        return self._context.playlists
