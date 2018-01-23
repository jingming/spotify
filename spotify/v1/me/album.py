from spotify import values
from spotify.page import Page
from spotify.resource import Instance, Resource


class SavedAlbum(Instance):

    @property
    def added_at(self):
        return self.property('added_at')

    @property
    def album(self):
        from spotify.v1.album import AlbumInstance
        return AlbumInstance(self.version, self.property('album'))


class AlbumList(Resource):

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
