from spotify import values
from spotify.object.context import Context
from spotify.page import Page
from spotify.resource import Instance, Resource


class RecentlyPlayedInstance(Instance):

    @property
    def track(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self.version, self.property('track'))

    @property
    def played_at(self):
        return self.property('played_at')

    @property
    def context(self):
        return Context.from_json(self.property('context'))


class RecentlyPlayedList(Resource):

    def list(self, limit=values.UNSET, after=values.UNSET, before=values.UNSET):
        params = values.of({
            'limit': limit,
            'after': after,
            'before': before
        })
        response = self.version.request('GET', '/me/player/recently-played', params=params)
        return RecentlyPlayedPage(self.version, response.json(), 'items')


class RecentlyPlayedPage(Page):

    @property
    def instance_class(self):
        return RecentlyPlayedInstance
