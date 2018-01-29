from spotify import values
from spotify.object.copyright import Copyright
from spotify.object.image import Image
from spotify.page import Page
from spotify.resource import Resource, UpgradableInstance
from spotify.v1.album.track import TrackList, TrackPage


class AlbumContext(Resource):

    def __init__(self, version, id):
        """
        Album context

        :param V1 version: Spotify API Version
        :param str id: Album id
        """
        super(AlbumContext, self).__init__(version)
        self.id = id

        self._tracks = None

    @property
    def tracks(self):
        """
        Tracks list context

        :return: Tracks list context
        """
        if self._tracks is None:
            self._tracks = TrackList(self.version, self.id)

        return self._tracks

    def fetch(self, market=values.UNSET):
        """
        Fetch the album metadata

        :param str market: Market locale
        :return: Fetched album instance
        :rtype: AlbumInstance
        """
        params = values.of({
            'market': market
        })
        response = self.version.request('GET', '/albums/{}'.format(self.id), params=params)
        return AlbumInstance(self.version, response.json())


class AlbumInstance(UpgradableInstance):

    @property
    def album_type(self):
        return self.property('album_type')

    @property
    def artists(self):
        from spotify.v1.artist import ArtistInstance
        return [ArtistInstance(self.version, artist) for artist in self.property('artists')]

    @property
    def available_markets(self):
        return self.property('available_markets')

    @property
    def copyrights(self):
        return [Copyright.from_json(copyright) for copyright in self.property('copyrights')]

    @property
    def external_ids(self):
        return self.property('external_ids')

    @property
    def external_urls(self):
        return self.property('external_urls')

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
    def release_date(self):
        return self.property('release_date')

    @property
    def release_date_precision(self):
        return self.property('release_date_precision')

    @property
    def tracks(self):
        return TrackPage(self.version, self.property('tracks'), 'items')

    @property
    def type(self):
        return self.property('type')

    @property
    def uri(self):
        return self.property('uri')


class AlbumList(Resource):

    def get(self, id):
        """
        Get the Album context

        :param str id: ID of the album
        :return: Album context
        :rtype: AlbumContext
        """
        return AlbumContext(self.version, id)

    def list(self, ids, market=values.UNSET):
        """
        List albums

        :param List[str] ids: List of albums ids
        :param str market: Market locale
        :return: Page of Albums
        :rtype: AlbumPage
        """
        params = values.of({
            'ids': ','.join(ids),
            'market': market
        })
        response = self.version.request('GET', '/albums', params=params)
        return AlbumPage(self.version, response.json(), 'albums')


class AlbumPage(Page):

    @property
    def instance_class(self):
        """
        Returns the AlbumInstance class

        :return: AlbumInstance class
        """
        return AlbumInstance
