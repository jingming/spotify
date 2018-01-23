from spotify.resource import Resource


class ImageList(Resource):

    def __init__(self, version, user_id, playlist_id):
        super(ImageList, self).__init__(version)
        self.user_id = user_id
        self.playlist_id = playlist_id

    def replace(self, image):
        response = self.version.requset(
            'POST',
            '/users/{}/playlists/{}/images'.format(self.user_id, self.playlist_id),
            data=image,
            headers={
                'Content-Type': 'image/jpeg'
            }
        )
        return response.status_code == 202
