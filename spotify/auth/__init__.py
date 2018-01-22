import time


class Token(object):

    def __init__(self, access_token, token_type, scope, expires_in, refresh_token):
        self.access_token = access_token
        self.token_type = token_type
        self.refresh_token = refresh_token
        self.scopes = scope.split(' ') if scope else []
        self.expires_at = int(time.time()) + expires_in

    @property
    def expired(self):
        return int(time.time()) > self.expires_at

    @classmethod
    def from_json(cls, json):
        return Token(
            json['access_token'],
            json['token_type'],
            json.get('scope', []),
            json['expires_in'],
            json.get('refresh_token', [])
        )


class TokenExpired(Exception):
    pass
