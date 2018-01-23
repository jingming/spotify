from spotify import values
from spotify.page import Page
from spotify.resource import Resource


class FollowingList(Resource):

    def list(self, type, limit=values.UNSET, after=values.UNSET):
        params = values.of({
            'type': type,
            'limit': limit,
            'after': after
        })
        response = self.version.request('GET', '/me/following', params=params)
        return FollowingPage(self.version, response.json(), 'items')

    def add(self, ids=values.UNSET):
        data = values.of({
            'ids': ids
        })
        response = self.version.request('PUT', '/me/following', data=data)
        return response.status_code == 204

    def remove(self, ids=values.UNSET):
        data = values.of({
            'ids': ids
        })
        response = self.version.request('DELETE', '/me/following', data=data)
        return response.status_code == 204

    def contains(self, type, ids):
        params = values.of({
            'type': type,
            'ids': ids
        })
        response = self.version.request('GET', '/me/following/contains', params=params)
        return response.json()


class FollowingPage(Page):

    @property
    def instance_class(self):
        from spotify.v1.artist import ArtistInstance
        return ArtistInstance
