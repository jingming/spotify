from spotify import values
from spotify.page import Page


class SavedAlbum(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def added_at(self):
        return self._properties['added_at']

    @property
    def album(self):
        from spotify.v1.album import AlbumInstance
        return AlbumInstance(self.version, self._properties['album'])


class AlbumList(object):

    def __init__(self, version):
        self.version = version

    def list(self, limit=values.UNSET, offset=values.UNSET, market=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset,
            'market': market
        })
        response = self.version.request('GET', '/me/albums', params=params)
        return AlbumPage(self.version, response.json(), 'items')

    def save(self, ids=values.UNSET):
        data = values.of({
            'ids': ids
        })
        response = self.version.request('PUT', '/me/albums', data=data)
        return response.status_code == 201

    def remove(self, ids=values.UNSET):
        data = values.of({
            'ids': ids
        })
        response = self.version.request('DELETE', '/me/albums', data=data)
        return response.status_code == 200

    def contains(self, ids=values.UNSET):
        params = values.of({
            'ids': ','.join(ids)
        })
        response = self.version.request('GET', '/me/albums/contains', params=params)
        return response.json()


class AlbumPage(Page):

    @property
    def instance_class(self):
        return SavedAlbum