from spotify import values
from spotify.page import Page


class TrackList(object):

    def __init__(self, version):
        self.version = version

    def list(self, limit=values.UNSET, offset=values.UNSET, time_range=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset,
            'time_range': time_range
        })
        response = self.version.request('GET', '/me/top/tracks', params=params)
        return TrackPage(self.version, response.json(), 'items')


class TrackPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance
