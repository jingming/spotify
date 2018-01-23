from spotify.object.device import Device
from spotify.page import Page
from spotify.resource import Resource


class DeviceInstance(Resource):

    def __init__(self, version, properties):
        super(DeviceInstance, self).__init__(version)
        self._device = Device.from_json(properties)

    @property
    def id(self):
        return self._device.id

    @property
    def is_active(self):
        return self._device.is_active

    @property
    def is_restricted(self):
        return self._device.is_restricted

    @property
    def name(self):
        return self._device.name

    @property
    def type(self):
        return self._device.type

    @property
    def volume_percent(self):
        return self._device.volume_percent


class DeviceList(Resource):

    def list(self):
        response = self.version.request('GET', '/me/player/devices')
        return DevicePage(self.version, response.json(), 'devices')


class DevicePage(Page):

    @property
    def instance_class(self):
        return DeviceInstance
