from spotify import values


class FeaturedPlaylistInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def message(self):
        return self._properties['message']

    @property
    def playlists(self):
        from spotify.v1.user.playlist import PlaylistPage
        return PlaylistPage(self.version, self._properties['playlists'], 'items')


class FeaturedPlaylistContext(object):

    def __init__(self, version):
        self.version = version

    def get(self, locale=values.UNSET, country=values.UNSET, timestamp=values.UNSET,
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
