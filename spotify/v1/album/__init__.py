from spotify import values
from spotify.object.copyright import Copyright
from spotify.object.image import Image
from spotify.page import Page
from spotify.v1.album.track import TrackList
from spotify.v1.artist import ArtistPage, ArtistInstance
from spotify.v1.track import TrackPage


class AlbumContext(object):

    def __init__(self, version, id):
        self.version = version
        self.id = id

        self._tracks = None

    @property
    def tracks(self):
        if self._tracks is None:
            self._tracks = TrackList(self.version, self.id)

        return self._tracks

    def fetch(self, market=values.UNSET):
        params = values.of({
            'market': market
        })
        response = self.version.request('GET', '/albums/{}'.format(self.id), params=params)
        return AlbumInstance(self.version, response.json())


class AlbumInstance(object):
    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    def refresh(self):
        response = self.version.client.request('GET', self.href)
        self._properties = response.json()

    @property
    def album_type(self):
        return self._properties['album_type']

    @property
    def artists(self):
        return [ArtistInstance(self.version, artist) for artist in self._properties['artists']]

    @property
    def available_markets(self):
        return self._properties['available_markets']

    @property
    def copyrights(self):
        return [Copyright.from_json(copyright) for copyright in self._properties['copyrights']]

    @property
    def external_ids(self):
        return self._properties['external_ids']

    @property
    def external_urls(self):
        return self._properties['external_urls']

    @property
    def genres(self):
        return self._properties['genres']

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
    def popularity(self):
        return self._properties['popularity']

    @property
    def release_date(self):
        return self._properties['release_date']

    @property
    def release_date_precision(self):
        return self._properties['release_date_precision']

    @property
    def tracks(self):
        return TrackPage(self.version, self._properties['tracks'], 'items')

    @property
    def type(self):
        return self._properties['type']

    @property
    def uri(self):
        return self._properties['uri']


class AlbumList(object):

    def __init__(self, version):
        self.version = version

    def get(self, id):
        return AlbumContext(self.version, id)

    def list(self, ids, market=values.UNSET):
        params = values.of({
            'ids': ','.join(ids),
            'market': market
        })
        response = self.version.request('GET', '/albums', params=params)
        return AlbumPage(self.version, response.json(), 'albums')


class AlbumPage(Page):
    INSTANCE_CLASS = AlbumInstance
