from spotify import values
from spotify.page import Page
from spotify.resource import Resource


class AlbumList(Resource):

    def __init__(self, version, artist_id):
        super(AlbumList, self).__init__(version)
        self.artist_id = artist_id

    def list(self, album_type=values.UNSET, market=values.UNSET, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'album_type': album_type,
            'market': market,
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/artist/{}/albums'.format(self.artist_id), params=params)
        return AlbumPage(self.version, response.json(), 'items')


class AlbumPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.album import AlbumInstance
        return AlbumInstance
