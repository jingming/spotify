import time


class Token(object):

    def __init__(self, access_token, token_type, scope, expires_in, refresh_token):
        """
        Access Token object

        :param str access_token : Access Token string
        :param str token_type: Type of token (user, client)
        :param str scope: Token permissions
        :param int expires_in: Time in seconds token is valid for
        :param bool refresh_token: Refresh to token upon expiration
        """
        self.access_token = access_token
        self.token_type = token_type
        self.refresh_token = refresh_token
        self.scopes = scope.split(' ') if scope else []
        self.expires_at = int(time.time()) + expires_in

    @property
    def expired(self):
        """
        Returns True if the token is expired

        :return: True if the token is expired
        """
        return int(time.time()) > self.expires_at

    @classmethod
    def from_json(cls, json):
        """
        Build a access token from JSON

        :param json: JSON blob
        :return: Access Token object
        :rtype: Token
        """
        return Token(
            json['access_token'],
            json['token_type'],
            json.get('scope', []),
            json['expires_in'],
            json.get('refresh_token', [])
        )


class TokenExpired(Exception):
    pass
