from spotify import values
from spotify.resource import Instance, Resource


class FeaturedPlaylistInstance(Instance):

    @property
    def message(self):
        return self.property('message')

    @property
    def playlists(self):
        from spotify.v1.user.playlist import PlaylistPage
        return PlaylistPage(self.version, self.property('playlists'), 'items')


class FeaturedPlaylistContext(Resource):

    def fetch(self, locale=values.UNSET, country=values.UNSET, timestamp=values.UNSET,
              limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'locale': locale,
            'country': country,
            'timestamp': timestamp,
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/browse/featured-playlists', params=params)
        return FeaturedPlaylistInstance(self.version, response.json())
