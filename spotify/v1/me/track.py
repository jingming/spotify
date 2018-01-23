from spotify import values
from spotify.page import Page


class SavedTrack(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def added_at(self):
        return self._properties['added_at']

    @property
    def track(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self.version, self._properties['track'])


class TrackList(object):

    def __init__(self, version):
        self.version = version

    def list(self, limit=values.UNSET, offset=values.UNSET, market=values.UNSET):
        params = values.of({
            'limit': limit,
            'offset': offset,
            'market': market
        })
        response = self.version.request('GET', '/me/tracks', params=params)
        return TrackPage(self.version, response.json(), 'items')

    def save(self, ids=values.UNSET):
        data = values.of({
            'ids': ids
        })
        response = self.version.request('PUT', '/me/tracks', data=data)
        return response.status_code == 200

    def remove(self, ids=values.UNSET):
        data = values.of({
            'ids': ids
        })
        response = self.version.request('DELETE', '/me/tracks', data=data)
        return response.status_code == 200

    def contains(self, ids=values.UNSET):
        params = values.of({
            'ids': ','.join(ids)
        })
        response = self.version.request('GET', '/me/tracks/contains', params=params)
        return response.json()


class TrackPage(Page):

    @property
    def instance_class(self):
        return SavedTrack
