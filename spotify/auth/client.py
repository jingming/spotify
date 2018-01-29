import os

from spotify.auth import Token, TokenExpired
from spotify.http import HttpClient


class Client(object):
    URL = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id=None, client_secret=None, auto_refresh=True, http_client=None):
        """
        Client Token object

        :param str client_id: Spotify Client ID
        :param str client_secret: Spotify Client secret
        :param bool auto_refresh: Automatically refresh the token
        :param http_client: HTTP Client to make requests
        """
        self.client_id = client_id or os.environ.get('SPOTIFY_CLIENT_ID')
        self.client_secret = client_secret or os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.http_client = http_client or HttpClient()
        self.auto_refresh = auto_refresh

        self._token = None

    @property
    def auth_string(self):
        """
        Get the auth string. If the token is expired and auto refresh enabled,
        a new token will be fetched

        :return: the auth string
        :rtype: str
        """
        if not self._token:
            self.execute()

        if not self._token.expired:
            return 'Bearer {}'.format(self._token.access_token)

        if self.auto_refresh:
            self.execute()
            return 'Bearer {}'.format(self._token.access_token)

        raise TokenExpired()

    def execute(self):
        """
        Fetch the token.
        """
        response = self.http_client.post(self.URL, data={
            'grant_type': 'client_credentials'
        }, auth=(self.client_id, self.client_secret))
        response.raise_for_status()
        self._token = Token.from_json(response.json())
