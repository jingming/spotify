from spotify.resource import Resource


class FollowerList(Resource):

    def __init__(self, version, user_id, playlist_id):
        super(FollowerList, self).__init__(version)
        self.user_id = user_id
        self.playlist_id = playlist_id

    def contains(self, ids=None):
        params = {}
        if ids:
            params['ids'] = ','.join(ids)

        response = self.version.request(
            'GET',
            '/users/{}/playlists/{}/followers/contains'.format(self.user_id, self.playlist_id),
            params=params
        )
        return response.json()
