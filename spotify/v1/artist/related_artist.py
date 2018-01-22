from spotify.page import Page


class RelatedArtistList(object):

    def __init__(self, version, artist_id):
        self.version = version
        self.artist_id = artist_id

    def list(self):
        response = self.version.request('GET', '/artist/{}/related-artists'.format(self.artist_id))
        return RelatedArtistPage(self.version, response.json(), 'artists')


class RelatedArtistPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.artist import ArtistInstance
        return ArtistInstance
