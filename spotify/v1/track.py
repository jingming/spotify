from spotify import values
from spotify.page import Page
from spotify.resource import Resource, UpgradableInstance


class TrackContext(Resource):

    def __init__(self, version, id):
        super(TrackContext, self).__init__(version)
        self.id = id

    def fetch(self, market=values.UNSET):
        params = values.of({
            'market': market
        })
        response = self.version.request('GET', '/tracks/{}'.format(self.id), params=params)
        return TrackInstance(self.version, response.json())


class TrackInstance(UpgradableInstance):

    @property
    def artists(self):
        from spotify.v1.artist import ArtistInstance
        return [ArtistInstance(self.version, artist) for artist in self.property('artists')]

    @property
    def available_markets(self):
        return self.property('available_markets')

    @property
    def disc_number(self):
        return self.property('disc_number')

    @property
    def duration_ms(self):
        return self.property('duration_ms')

    @property
    def explicit(self):
        return self.property('explicit')

    @property
    def external_urls(self):
        return self.property('external_urls')

    @property
    def id(self):
        return self.property('id')

    @property
    def name(self):
        return self.property('name')

    @property
    def preview_url(self):
        return self.property('preview_url')

    @property
    def track_number(self):
        return self.property('track_number')

    @property
    def type(self):
        return self.property('type')

    @property
    def uri(self):
        return self.property('uri')


class TrackList(Resource):

    def get(self, id):
        return TrackContext(self.version, id)

    def list(self, ids, market=values.UNSET):
        params = values.of({
            'ids': ','.join(ids),
            'market': market
        })

        response = self.version.request('GET', '/tracks', params=params)
        return TrackPage(self.version, response.json(), 'tracks')


class TrackPage(Page):

    @property
    def instance_class(self):
        return TrackInstance
