

class Followers(object):

    def __init__(self, href, total):
        self.href = href
        self.total = total

    @classmethod
    def from_json(cls, json):
        return Followers(
            json['href'],
            json['total']
        )
