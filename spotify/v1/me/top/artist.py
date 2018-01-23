from spotify import values
from spotify.page import Page


class ArtistList(object):

    def __init__(self, version):
        self.version = version

    def list(self, limit=values.UNSET, offset=values.UNSET, time_range=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset,
            'time_range': time_range
        })
        response = self.version.request('GET', '/me/top/artists', params=params)
        return ArtistPage(self.version, response.json(), 'items')


class ArtistPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.artist import ArtistInstance
        return ArtistInstance
