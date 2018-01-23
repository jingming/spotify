from spotify.resource import Resource


class AvailableGenreSeedsContext(Resource):

    def fetch(self):
        response = self.version.request('GET', '/recommendations/available-genre-seeds')
        return response.json()['genres']
