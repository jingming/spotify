from spotify import values
from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.page import Page
from spotify.v1.user.playlist.follower import FollowerList
from spotify.v1.user.playlist.image import ImageList
from spotify.v1.user.playlist.track import PlaylistTrackList, PlaylistTrackPage


class PlaylistInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties
        self._context = PlaylistContext(self.version, self.owner.id, self.id)

    def refresh(self):
        response = self.version.client.request('GET', self.href)
        self._properties = response.json()

    @property
    def collaborative(self):
        return self._properties['collaborative']

    @property
    def description(self):
        return self._properties['description']

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
    def name(self):
        return self._properties['name']

    @property
    def owner(self):
        from spotify.v1.user import UserInstance
        return UserInstance(self.version, self._properties['owner'])

    @property
    def public(self):
        return self._properties['public']

    @property
    def snapshot_id(self):
        return self._properties['snapshot_id']

    @property
    def tracks_(self):
        return PlaylistTrackPage(self.version, self._properties['tracks'], 'items')

    @property
    def type(self):
        return self._properties['type']

    @property
    def uri(self):
        return self._properties['uri']

    @property
    def followers(self):
        return self._context.followers

    @property
    def images(self):
        return self._context.images

    @property
    def tracks(self):
        return self._context.tracks


class PlaylistContext(object):

    def __init__(self, version, user_id, id):
        self.version = version
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


class PlaylistList(object):

    def __init__(self, version, user_id):
        self.version = version
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
