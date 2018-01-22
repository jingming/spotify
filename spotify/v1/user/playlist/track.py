from spotify import values
from spotify.object.snapshot import Snapshot
from spotify.page import Page


class PlaylistTrackInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def added_at(self):
        return self._properties['added_at']

    @property
    def added_by(self):
        from spotify.v1.user import UserInstance
        return UserInstance(self.version, self._properties['added_by'])

    @property
    def is_local(self):
        return self._properties['is_local']

    @property
    def track(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self.version, self._properties['track'])


class PlaylistTrackList(object):

    def __init__(self, version, user_id, playlist_id):
        self.version = version
        self.user_id = user_id
        self.playlist_id = playlist_id

    def add(self, uris=values.UNSET, position=values.UNSET):
        data = values.of({
            'uris': uris,
            'position': position
        })
        response = self.version.request(
            'POST',
            '/users/{}/playlists/{}/tracks'.format(self.user_id, self.playlist_id),
            data=data
        )
        return Snapshot.from_json(response.json())

    def list(self, fields=values.UNSET, limit=values.UNSET, offset=values.UNSET, market=values.UNSET):
        params = values.of({
            'fields': fields,
            'limit': limit,
            'offset': offset,
            'market': market
        })
        response = self.version.request(
            'GET',
            '/users/{}/playlists/{}/tracks'.format(self.user_id, self.playlist_id),
            params=params
        )
        return PlaylistTrackPage(self.version, response.json(), 'items')

    def remove(self, tracks=values.UNSET, positions=values.UNSET, snapshot_id=values.UNSET):
        data = values.of({
            'tracks': tracks,
            'positions': positions,
            'snapshot_id': snapshot_id
        })
        response = self.version.request(
            'DELETE',
            '/users/{}/playlists/{}/tracks'.format(self.user_id, self.playlist_id),
            data=data
        )
        return Snapshot.from_json(response.json())

    def reorder(self, range_start, insert_before, range_length=values.UNSET, snapshot_id=values.UNSET):
        data = values.of({
            'range_start': range_start,
            'insert_before': insert_before,
            'range_length': range_length,
            'snapshot_id': snapshot_id
        })
        response = self.version.request(
            'PUT',
            '/users/{}/playlists/{}/tracks'.format(self.user_id, self.playlist_id),
            data=data
        )
        return Snapshot.from_json(response.json())

    def replace(self, uris=values.UNSET):
        data = values.of({
            'uris': uris
        })
        response = self.version.request(
            'PUT',
            '/users/{}/playlists/{}/tracks'.format(self.user_id, self.playlist_id),
            data=data
        )
        return response.status_code == 201


class PlaylistTrackPage(Page):

    @property
    def instance_class(self):
        return PlaylistTrackInstance
