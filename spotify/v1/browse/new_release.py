from spotify import values
from spotify.page import Page
from spotify.resource import Resource


class NewReleaseList(Resource):

    def list(self, country=values.UNSET, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'country': country,
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/browse/new-releases', params=params)
        return NewReleasePage(self.version, response.json()['albums'], 'items')


class NewReleasePage(Page):

    @property
    def instance_class(self):
        from spotify.v1.album import AlbumInstance
        return AlbumInstance
