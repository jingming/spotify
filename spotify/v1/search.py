from spotify import values
from spotify.resource import Resource, Instance


class SearchContext(Resource):

    def get(self, q, types, market=values.UNSET, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'q': q,
            'type': ','.join(types),
            'market': market,
            'limit': limit,
            'offset': offset
        })

        response = self.version.request('GET', '/search', params=params)
        return SearchInstance(self.version, response.json())


class SearchInstance(Instance):

    @property
    def albums(self):
        from spotify.v1.album import AlbumPage
        return AlbumPage(self.version, self.property('albums', {}), 'items')

    @property
    def artists(self):
        from spotify.v1.artist import ArtistPage
        return ArtistPage(self.version, self.property('artists', {}), 'items')

    @property
    def playlists(self):
        from spotify.v1.user.playlist import PlaylistPage
        return PlaylistPage(self.version, self.property('playlists', {}), 'items')

    @property
    def tracks(self):
        from spotify.v1.track import TrackPage
        return TrackPage(self.version, self.property('tracks', {}), 'items')
