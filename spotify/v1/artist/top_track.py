from spotify.page import Page
from spotify.resource import Resource


class TopTrackList(Resource):

    def __init__(self, version, artist_id):
        super(TopTrackList, self).__init__(version)
        self.artist_id = artist_id

    def list(self, country):
        params = {
            'country': country
        }
        response = self.version.request('GET', '/artists/{}/top-tracks'.format(self.artist_id), params=params)
        return TopTrackPage(self.version, response.json(), 'tracks')


class TopTrackPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance
