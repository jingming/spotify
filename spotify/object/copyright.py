

class Copyright(object):

    def __init__(self, text, type):
        self.text = text
        self.type = type

    @classmethod
    def from_json(cls, json):
        return Copyright(
            json['text'],
            json['type']
        )
