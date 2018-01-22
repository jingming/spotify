

class Snapshot(object):

    def __init__(self, id):
        self.id = id

    @classmethod
    def from_json(cls, json):
        return Snapshot(
            json['snapshot_id']
        )
