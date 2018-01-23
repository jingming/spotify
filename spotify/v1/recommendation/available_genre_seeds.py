

class AvailableGenreSeedsContext(object):

    def __init__(self, version):
        self.version = version

    def fetch(self):
        response = self.version.request('GET', '/recommendations/available-genre-seeds')
        return response.json()['genres']
