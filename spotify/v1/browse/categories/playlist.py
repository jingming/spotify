from spotify import values
from spotify.page import Page
from spotify.resource import Resource


class PlaylistList(Resource):

    def __init__(self, version, category_id):
        super(PlaylistList, self).__init__(version)
        self.category_id = category_id

    def list(self, country=values.UNSET, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'country': country,
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/browse/categories/{}/playlists'.format(self.category_id), params=params)
        return PlaylistPage(self.version, response.json()['playlists'], 'items')


class PlaylistPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.user.playlist import PlaylistInstance
        return PlaylistInstance
