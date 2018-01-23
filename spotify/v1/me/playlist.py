from spotify import values
from spotify.page import Page
from spotify.resource import Resource


class PlaylistList(Resource):

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
