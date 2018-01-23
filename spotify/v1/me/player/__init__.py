from spotify import values
from spotify.object.context import Context
from spotify.object.device import Device
from spotify.resource import Resource, Instance
from spotify.v1.me.player.currently_playing import CurrentlyPlayingContext
from spotify.v1.me.player.device import DeviceList
from spotify.v1.me.player.recently_played import RecentlyPlayedList


class PlayerContext(Resource):

    def __init__(self, version):
        super(PlayerContext, self).__init__(version)

        self._currently_playing = None
        self._devices = None
        self._recently_played = None

    @property
    def currently_playing(self):
        if not self._currently_playing:
            self._currently_playing = CurrentlyPlayingContext(self.version)

        return self._currently_playing

    @property
    def devices(self):
        if not self._devices:
            self._devices = DeviceList(self.version)

        return self._devices

    @property
    def recently_played(self):
        if not self._recently_played:
            self._recently_played = RecentlyPlayedList(self.version)

        return self._recently_played

    def fetch(self, market=values.UNSET):
        params = values.of({
            'market': market
        })
        response = self.version.request('GET', '/me/player', params=params)
        return PlayerInstance(self.version, response.json())

    def transfer(self, device_ids, play=values.UNSET):
        data = values.of({
            'device_ids': device_ids,
            'play': play
        })
        response = self.version.request('PUT', '/me/player', data=data)
        return response.status_code == 204

    def play(self, device_id=values.UNSET, context_uri=values.UNSET, uris=values.UNSET, offset=values.UNSET):
        params = values.of({
            'device_id': device_id
        })
        data = values.of({
            'context_uri': context_uri,
            'uris': uris,
            'offset': offset
        })
        response = self.version.request('PUT', '/me/player/play', params=params, data=data)
        return response.status_code == 204

    def pause(self, device_id=values.UNSET):
        params = values.of({
            'device_id': device_id
        })
        response = self.version.request('PUT', '/me/player/pause', params=params)
        return response.status_code == 204

    def next_(self, device_id=values.UNSET):
        params = values.of({
            'device_id': device_id
        })
        response = self.version.request('POST', '/me/player/next', params=params)
        return response.status_code == 204

    def previous(self, device_id=values.UNSET):
        params = values.of({
            'device_id': device_id
        })
        response = self.version.request('POST', '/me/player/previous', params=params)
        return response.status_code == 204

    def seek(self, position_ms, device_id=values.UNSET):
        params = values.of({
            'position_ms': position_ms,
            'device_id': device_id
        })
        response = self.version.request('PUT', '/me/player/previous', params=params)
        return response.status_code == 204

    def repeat(self, state, device_id=values.UNSET):
        params = values.of({
            'state': state,
            'device_id': device_id
        })
        response = self.version.request('PUT', '/me/player/repeat', params=params)
        return response.status_code == 204

    def volume(self, volume_percent, device_id=values.UNSET):
        params = values.of({
            'volume_percent': volume_percent,
            'device_id': device_id
        })
        response = self.version.request('PUT', '/me/player/volume', params=params)
        return response.status_code == 204

    def shuffle(self, state, device_id=values.UNSET):
        params = values.of({
            'state': state,
            'device_id': device_id
        })
        response = self.version.request('PUT', '/me/player/shuffle', params=params)
        return response.status_code == 204


class PlayerInstance(Instance):

    def __init__(self, version, properties):
        super(PlayerInstance, self).__init__(version, properties)
        self._context = PlayerContext(self.version)

    @property
    def timestamp(self):
        return self.property('timestamp')

    @property
    def device(self):
        return Device.from_json(self.property('device'))

    @property
    def progress_ms(self):
        return self.property('progress_ms')

    @property
    def is_playing(self):
        return self.property('is_playing')

    @property
    def item(self):
        from spotify.v1.track import TrackInstance
        return TrackInstance(self.version, self.property('item'))

    @property
    def shuffle_state(self):
        return self.property('shuffle_state')

    @property
    def repeat_state(self):
        return self.property('repeat_state')

    @property
    def context(self):
        return Context.from_json(self.property('context'))

    @property
    def currently_playing(self):
        return self._context.currently_playing

    @property
    def devices(self):
        return self._context.devices

    @property
    def recently_played(self):
        return self._context.recently_played

    @property
    def transfer(self):
        return self._context.transfer

    @property
    def play(self):
        return self._context.play

    @property
    def pause(self):
        return self._context.pause

    @property
    def next_(self):
        return self._context.next_

    @property
    def previous(self):
        return self._context.previous

    @property
    def seek(self):
        return self._context.seek

    @property
    def volume(self):
        return self._context.volume

    @property
    def repeat(self):
        return self._context.repeat

    @property
    def shuffle(self):
        return self._context.shuffle
