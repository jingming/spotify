

class Context(object):

    def __init__(self, type, uri, href, external_urls):
        self.type = type
        self.uri = uri
        self.href = href
        self.external_urls = external_urls

    @classmethod
    def from_json(cls, json):
        return Context(
            json['type'],
            json['uri'],
            json['href'],
            json['external_urls']
        )
