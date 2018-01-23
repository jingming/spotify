from spotify import values
from spotify.page import Page


class PlaylistList(object):

    def __init__(self, version):
        self.version = version

    def list(self, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/me/playlists', params=params)
        return PlaylistPage(self.version, response.json(), 'items')


class PlaylistPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.user.playlist import PlaylistInstance
        return PlaylistInstance
