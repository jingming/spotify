from spotify import values
from spotify.object.context import Context
from spotify.resource import Resource, Instance


class CurrentlyPlayingContext(Resource):

    def fetch(self, market=values.UNSET):
        params = values.of({
            'market': market
        })
        response = self.version.request('GET', '/me/player/currently-playing', params=params)
        return CurrentlyPlayingInstance(self.version, response.json())


class CurrentlyPlayingInstance(Instance):

    @property
    def context(self):
        return Context(self.property('context'))

    @property
    def timestamp(self):
        return self.property('timestamp')

    @property
    def progress_ms(self):
        return self.property('progress_ms')

    @property
    def is_playing(self):
        return self.property('is_playing')

    @property
    def item(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self.version, self.property('item'))
