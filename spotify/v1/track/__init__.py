from spotify.page import Page
from spotify.v1.artist import ArtistInstance


class TrackContext(object):
    pass


class TrackInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    def refresh(self):
        response = self.version.request('GET', self.href)
        self._properties = response.json()

    @property
    def artists(self):
        return [ArtistInstance(self.version, artist) for artist in self._properties['artists']]

    @property
    def available_markets(self):
        return self._properties['available_markets']

    @property
    def disc_number(self):
        return self._properties['disc_number']

    @property
    def duration_ms(self):
        return self._properties['duration_ms']

    @property
    def explicit(self):
        return self._properties['explicit']

    @property
    def external_urls(self):
        return self._properties['external_urls']

    @property
    def href(self):
        return self._properties['href']

    @property
    def id(self):
        return self._properties['id']

    @property
    def name(self):
        return self._properties['name']

    @property
    def preview_url(self):
        return self._properties['preview_url']

    @property
    def track_number(self):
        return self._properties['track_number']

    @property
    def type(self):
        return self._properties['type']

    @property
    def uri(self):
        return self._properties['uri']


class TrackList(object):
    pass


class TrackPage(Page):
    INSTANCE_CLASS = TrackInstance
