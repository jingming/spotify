import os
import uuid
from spotify.auth import Token, TokenExpired
from spotify.http import HttpClient


def authorize_url(client_id=None, redirect_uri=None, state=None, scopes=None, show_dialog=False, http_client=None):
    """
    Trigger authorization dialog

    :param client_id: Client ID
    :param redirect_uri: Application Redirect URI
    :param state: Application State
    :param scopes: Scopes to request
    :param show_dialog: Show the dialog
    :param http_client: HTTP Client for requests
    :return str Authorize URL
    """
    params = {
        'client_id': client_id or os.environ.get('SPOTIFY_CLIENT_ID'),
        'redirect_uri': redirect_uri or os.environ.get('SPOTIFY_REDIRECT_URI'),
        'state': state or str(uuid.uuid4()).replace('-', ''),
        'scopes': ' '.join(scopes) if scopes else '',
        'show_dialog': show_dialog,
        'response_type': 'code'
    }
    query = ['{}={}'.format(k, v) for k, v in params.items()]
    return '{}?{}'.format('https://accounts.spotify.com/authorize', '&'.join(query))


class User(object):
    URL = 'https://accounts.spotify.com/api/token'

    def __init__(self, code, auto_refresh=True, client_id=None, client_secret=None,
                 redirect_uri=None, http_client=None):
        """
        User access token

        :param str code: Auth token code
        :param bool auto_refresh: Refresh the token upon expiration
        :param client_id: Client ID
        :param client_secret: Client Secret
        :param redirect_uri: Application Redirect URI
        :param http_client: HTTP Client for requests
        """
        self.code = code
        self.auto_refresh = auto_refresh
        self.client_id = client_id or os.environ.get('SPOTIFY_CLIENT_ID')
        self.client_secret = client_secret or os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = redirect_uri or os.environ.get('SPOTIFY_REDIRECT_URI')
        self.http_client = http_client or HttpClient()

        self._token = None
        """ :type : Token """

    @property
    def auth_string(self):
        if not self._token:
            self.execute()

        if not self._token.expired:
            return 'Bearer {}'.format(self._token.access_token)

        if self.auto_refresh:
            self.refresh()
            return 'Bearer {}'.format(self._token.access_token)

        raise TokenExpired()

    def refresh(self):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self._token.refresh_token
        }

        response = self.http_client.post(self.URL, data=data, auth=(self.client_id, self.client_secret))
        response.raise_for_status()
        self._token = Token.from_json(response.json())

    def execute(self):
        data = {
            'grant_type': 'authorization_code',
            'code': self.code,
            'redirect_uri': self.redirect_uri
        }

        response = self.http_client.post(self.URL, data=data, auth=(self.client_id, self.client_secret))
        response.raise_for_status()
        self._token = Token.from_json(response.json())
