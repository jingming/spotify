from spotify import values
from spotify.page import Page
from spotify.v1.album import AlbumInstance


class AlbumList(object):

    def __init__(self, version, artist_id):
        self.version = version
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
    INSTANCE_CLASS = AlbumInstance
