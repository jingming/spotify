from spotify.v1.me.top.artist import ArtistList
from spotify.v1.me.top.track import TrackList


class TopContext(object):

    def __init__(self, version):
        self.version = version

        self._artists = None
        self._tracks = None

    @property
    def artists(self):
        if not self._artists:
            self._artists = ArtistList(self.version)

        return self._artists

    @property
    def tracks(self):
        if not self._tracks:
            self._tracks = TrackList(self.version)

        return self._tracks
