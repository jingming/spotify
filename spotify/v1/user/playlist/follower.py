from spotify import values


class FollowerList(object):

    def __init__(self, version, user_id, playlist_id):
        self.version = version
        self.user_id = user_id
        self.playlist_id = playlist_id

    def contains(self, ids=values.UNSET):
        params = values.of({
            'ids': ids
        })
        response = self.version.request(
            'GET',
            '/users/{}/playlists/{}/followers/contains'.format(self.user_id, self.playlist_id),
            params=params
        )
        return response.json()
