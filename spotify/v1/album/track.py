from spotify import values
from spotify.page import Page
from spotify.resource import Resource


class TrackList(Resource):

    def __init__(self, version, album_id):
        super(TrackList, self).__init__(version)
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

    @property
    def instance_class(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance
