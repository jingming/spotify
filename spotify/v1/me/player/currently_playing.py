from spotify import values
from spotify.object.context import Context


class CurrentlyPlayingContext(object):

    def __init__(self, version):
        self.version = version

    def fetch(self, market=values.UNSET):
        params = values.of({
            'market': market
        })
        response = self.version.request('GET', '/me/player/currently-playing', params=params)
        return CurrentlyPlayingInstance(self.version, response.json())


class CurrentlyPlayingInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def context(self):
        return Context(self._properties['context'])

    @property
    def timestamp(self):
        return self._properties['timestamp']

    @property
    def progress_ms(self):
        return self._properties['progress_ms']

    @property
    def is_playing(self):
        return self._properties('is_playing')

    @property
    def item(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self.version, self._properties['item'])
