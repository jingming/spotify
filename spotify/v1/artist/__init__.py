from spotify.object.followers import Followers
from spotify.object.image import Image
from spotify.page import Page
from spotify.resource import Resource, UpgradableInstance
from spotify.v1.artist.album import AlbumList
from spotify.v1.artist.related_artist import RelatedArtistList
from spotify.v1.artist.top_track import TopTrackList


class ArtistContext(Resource):

    def __init__(self, version, id):
        super(ArtistContext, self).__init__(version)
        self.id = id

        self._albums = None
        self._top_tracks = None
        self._related_artists = None

    @property
    def albums(self):
        if not self._albums:
            self._albums = AlbumList(self.version, self.id)

        return self._albums

    @property
    def top_tracks(self):
        if not self._top_tracks:
            self._top_tracks = TopTrackList(self.version, self.id)

        return self.top_tracks

    @property
    def related_artists(self):
        if not self._related_artists:
            self._related_artists = RelatedArtistList(self.version, self.id)

        return self._related_artists

    def fetch(self):
        response = self.version.request('GET', '/artists/{}'.format(self.id))
        return ArtistInstance(self.version, response.json())


class ArtistInstance(UpgradableInstance):

    def __init__(self, version, properties):
        super(ArtistInstance, self).__init__(version, properties)
        self._context = ArtistContext(self.version, self.id)

    @property
    def external_urls(self):
        return self.property('external_urls')

    @property
    def followers(self):
        return Followers.from_json(self.property('followers'))

    @property
    def genres(self):
        return self.property('genres')

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
    def popularity(self):
        return self.property('popularity')

    @property
    def type(self):
        return self.property('type')

    @property
    def uri(self):
        return self.property('uri')

    @property
    def albums(self):
        return self._context.albums

    @property
    def top_tracks(self):
        return self._context.top_tracks

    @property
    def related_artists(self):
        return self._context.related_artists


class ArtistList(Resource):

    def get(self, id):
        return ArtistContext(self.version, id)

    def list(self, ids):
        response = self.version.request('GET', '/artists', params={
            'ids': ','.join(ids)
        })
        return ArtistPage(self.version, response.json(), 'artists')


class ArtistPage(Page):

    @property
    def instance_class(self):
        return ArtistInstance
