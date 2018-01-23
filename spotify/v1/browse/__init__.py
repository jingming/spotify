from spotify.resource import Resource
from spotify.v1.browse.featured_playlist import FeaturedPlaylistContext
from spotify.v1.browse.new_release import NewReleaseList


class BrowseContext(Resource):

    def __init__(self, version):
        super(BrowseContext, self).__init__(version)

        self._featured_playlists = None
        self._new_releases = None
        self._categories = None

    @property
    def featured_playlists(self):
        if not self._featured_playlists:
            self._featured_playlists = FeaturedPlaylistContext(self.version)

        return self._featured_playlists

    @property
    def new_releases(self):
        if not self._new_releases:
            self._new_releases = NewReleaseList(self.version)

        return self._new_releases
