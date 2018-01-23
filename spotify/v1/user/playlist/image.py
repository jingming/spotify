

class ImageList(object):

    def __init__(self, version, user_id, playlist_id):
        self.version = version
        self.user_id = user_id
        self.playlist_id = playlist_id

    def replace(self, image):
        response = self.version.requset(
            'POST',
            '/users/{}/playlists/{}/images'.format(self.user_id, self.playlist_id),
            data=image
        )
        return response.status_code == 202
