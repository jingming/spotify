from spotify.page import Page
from spotify.v1.track import TrackInstance


class TopTrackList(object):

    def __init__(self, version, artist_id):
        self.version = version
        self.artist_id = artist_id

    def list(self, country):
        params = {
            'country': country
        }
        response = self.version.request('GET', '/artists/{}/top-tracks'.format(self.artist_id), params=params)
        return TopTrackPage(self.version, response.json(), 'tracks')


class TopTrackPage(Page):
    INSTANCE_CLASS = TrackInstance
