from spotify import values
from spotify.page import Page
from spotify.v1.track import TrackInstance


class TrackList(object):

    def __init__(self, version, album_id):
        self.version = version
        self.album_id = album_id

    def list(self, limit=values.UNSET, offset=values.UNSET, market=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset,
            'market': market
        })
        response = self.version.request('GET', '/albums/{}/tracks'.format(self.album_id), params=params)
        return TrackPage(self.version, response.json(), 'items')


class TrackPage(Page):
    INSTANCE_CLASS = TrackInstance
