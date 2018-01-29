import os
import uuid
from spotify.auth import Token, TokenExpired
from spotify.http import HttpClient


def authorize_url(client_id=None, redirect_uri=None, state=None, scopes=None, show_dialog=False, http_client=None):
    """
    Trigger authorization dialog

    :param str client_id: Client ID
    :param str redirect_uri: Application Redirect URI
    :param str state: Application State
    :param List[str] scopes: Scopes to request
    :param bool show_dialog: Show the dialog
    :param http_client: HTTP Client for requests
    :return str Authorize URL
    :rtype str
    """
    params = {
        'client_id': client_id or os.environ.get('SPOTIFY_CLIENT_ID'),
        'redirect_uri': redirect_uri or os.environ.get('SPOTIFY_REDIRECT_URI'),
        'state': state or str(uuid.uuid4()).replace('-', ''),
        'scope': ' '.join(scopes) if scopes else '',
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
        :param str client_id: Client ID
        :param str client_secret: Client Secret
        :param str redirect_uri: Application Redirect URI
        :param http_client: HTTP Client for requests
        """
        self.code = code
        self.auto_refresh = auto_refresh
        self.client_id = client_id or os.environ.get('SPOTIFY_CLIENT_ID')
        self.client_secret = client_secret or os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = redirect_uri or os.environ.get('SPOTIFY_REDIRECT_URI')
        self.http_client = http_client or HttpClient()

        self._token = None

    @property
    def auth_string(self):
        """
        Get the auth string. If token is expired and auto refresh enabled,
        a new token will be fetched

        :return: the auth string
        :rtype: str
        """
        if not self._token:
            self.execute()

        if not self._token.expired:
            return 'Bearer {}'.format(self._token.access_token)

        if self.auto_refresh:
            self.refresh()
            return 'Bearer {}'.format(self._token.access_token)

        raise TokenExpired()

    def refresh(self):
        """
        Refresh the access token
        """
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self._token.refresh_token
        }

        response = self.http_client.post(self.URL, data=data, auth=(self.client_id, self.client_secret))
        response.raise_for_status()
        self._token = Token.from_json(response.json())

    def execute(self):
        """
        Fetch the access token
        """
        data = {
            'grant_type': 'authorization_code',
            'code': self.code,
            'redirect_uri': self.redirect_uri
        }

        response = self.http_client.post(self.URL, data=data, auth=(self.client_id, self.client_secret))
        response.raise_for_status()
        self._token = Token.from_json(response.json())
