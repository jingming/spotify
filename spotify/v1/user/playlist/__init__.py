from spotify import values
from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.page import Page
from spotify.resource import UpgradableInstance, Resource
from spotify.v1.user.playlist.follower import FollowerList
from spotify.v1.user.playlist.image import ImageList
from spotify.v1.user.playlist.track import PlaylistTrackList, PlaylistTrackPage


class PlaylistInstance(UpgradableInstance):

    def __init__(self, version, properties):
        super(PlaylistInstance, self).__init__(version, properties)
        self._context = PlaylistContext(self.version, self.owner.id, self.id)

    @property
    def collaborative(self):
        return self.property('collaborative')

    @property
    def description(self):
        return self.property('description')

    @property
    def external_urls(self):
        return self.property('external_urls')

    @property
    def followers(self):
        return Followers.from_json(self.property('followers'))

    @property
    def id(self):
        return self.property('id')

    @property
    def images(self):
        return [Image.from_json(image) for image in self.property('images')]

    @property
    def name(self):
        return self.property('name')

    @property
    def owner(self):
        from spotify.v1.user import UserInstance
        return UserInstance(self.version, self.property('owner'))

    @property
    def public(self):
        return self.property('public')

    @property
    def snapshot_id(self):
        return self.property('snapshot_id')

    @property
    def tracks_(self):
        return PlaylistTrackPage(self.version, self.property('tracks'), 'items')

    @property
    def type(self):
        return self.property('type')

    @property
    def uri(self):
        return self.property('uri')

    @property
    def tracks(self):
        return self._context.tracks

    @property
    def update(self):
        return self._context.update

    @property
    def follow(self):
        return self._context.follow

    @property
    def unfollow(self):
        return self._context.unfollow


class PlaylistContext(Resource):

    def __init__(self, version, user_id, id):
        super(PlaylistContext, self).__init__(version)
        self.user_id = user_id
        self.id = id

        self._followers = None
        self._images = None
        self._tracks = None

    @property
    def followers(self):
        if not self._followers:
            self._followers = FollowerList(self.version, self.user_id, self.id)

        return self._followers

    @property
    def images(self):
        if not self._images:
            self._images = ImageList(self.version, self.user_id, self.id)

        return self._images

    @property
    def tracks(self):
        if not self._tracks:
            self._tracks = PlaylistTrackList(self.version, self.user_id, self.id)

        return self._tracks

    def fetch(self, fields=values.UNSET, market=values.UNSET):
        params = values.of({
            'fields': fields,
            'market': market
        })
        response = self.version.request('GET', '/users/{}/playlists/{}'.format(self.user_id, self.id), params=params)
        return PlaylistInstance(self.version, response.json())

    def update(self, name=values.UNSET, public=values.UNSET, collaborative=values.UNSET, description=values.UNSET):
        data = values.of({
            'name': name,
            'public': public,
            'collaborative': collaborative,
            'description': description
        })
        response = self.version.request('PUT', '/users/{}/playlists/{}'.format(self.user_id, self.id), data=data)
        return response.status_code == 200

    def unfollow(self):
        response = self.version.request(
            'DELETE',
            '/users/{}/playlists/{}/followers'.format(self.user_id, self.id)
        )
        return response.status_code == 200

    def follow(self, public=values.UNSET):
        data = values.of({
            'public': public
        })
        response = self.version.request(
            'PUT',
            '/users/{}/playlists/{}/followers'.format(self.user_id, self.id),
            data=data
        )
        return response.status_code == 200


class PlaylistList(Resource):

    def __init__(self, version, user_id):
        super(PlaylistList, self).__init__(version)
        self.user_id = user_id

    def create(self, name, public=values.UNSET, collaborative=values.UNSET, description=values.UNSET):
        data = values.of({
            'name': name,
            'public': public,
            'collaborative': collaborative,
            'description': description
        })
        response = self.version.request('POST', '/users/{}/playlists'.format(self.user_id), data=data)
        return PlaylistInstance(self.version, response.json())

    def list(self, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/users/{}/playlists'.format(self.user_id), params=params)
        return PlaylistPage(self.version, response.json(), 'items')

    def get(self, id):
        return PlaylistContext(self.version, self.user_id, id)


class PlaylistPage(Page):

    @property
    def instance_class(self):
        return PlaylistInstance
