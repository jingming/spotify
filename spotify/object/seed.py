

class Seed(object):

    def __init__(self, initial_pool_size, after_filtering_size, after_relinking_size, href, id, type):
        self.initial_pool_size = initial_pool_size
        self.after_filtering_size = after_filtering_size
        self.after_relinking_size = after_relinking_size
        self.href = href
        self.id = id
        self.type = type

    @classmethod
    def from_json(cls, json):
        return Seed(
            json['initialPoolSize'],
            json['afterFilteringSize'],
            json['afterRelinkingSize'],
            json['href'],
            json['id'],
            json['type']
        )
