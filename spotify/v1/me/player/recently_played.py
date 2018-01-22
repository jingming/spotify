from spotify import values
from spotify.object.context import Context
from spotify.page import Page


class RecentlyPlayedInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def track(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self._properties['track'])

    @property
    def played_at(self):
        return self._properties['played_at']

    @property
    def context(self):
        return Context.from_json(self._properties['context'])


class RecentlyPlayedList(object):

    def __init__(self, version):
        self.version = version

    def list(self, limit=values.UNSET, after=values.UNSET, before=values.UNSET):
        params = values.of({
            'limit': limit,
            'after': after,
            'before': before
        })
        response = self.version.request('GET', '/me/player/recently-played', params=params)
        return RecentlyPlayedPage(self.version, response.json(), 'items')


class RecentlyPlayedPage(Page):
    INSTANCE_CLASS = RecentlyPlayedInstance
