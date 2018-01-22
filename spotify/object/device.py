

class Device(object):

    def __init__(self, id, is_active, is_restricted, name, type, volume_percent):
        self.id = id
        self.is_active = is_active
        self.is_restricted = is_restricted
        self.name = name
        self.type = type,
        self.volume_percent = volume_percent

    @classmethod
    def from_json(cls, json):
        return Device(
            json['id'],
            json['is_active'],
            json['is_restricted'],
            json['name'],
            json['type'],
            json['volume_percent']
        )
