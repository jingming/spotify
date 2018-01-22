

class Image(object):

    def __init__(self, height, width, url):
        self.height = height
        self.width = width
        self.url = url

    @classmethod
    def from_json(cls, json):
        return Image(
            json['height'],
            json['width'],
            json['url']
        )
