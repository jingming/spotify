from spotify.page import Page
from spotify.v1.artist import ArtistInstance


class RelatedArtistList(object):

    def __init__(self, version, artist_id):
        self.version = version
        self.artist_id = artist_id

    def list(self):
        response = self.version.request('GET', '/artist/{}/related-artists'.format(self.artist_id))
        return RelatedArtistPage(self.version, response.json(), 'artists')


class RelatedArtistPage(Page):
    INSTANCE_CLASS = ArtistInstance
