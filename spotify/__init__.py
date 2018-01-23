import json

from spotify.http import HttpClient
from spotify.v1 import V1


class Client:
    API = 'https://api.spotify.com'

    def __init__(self, auth, http_client=None):
        self.auth = auth
        self.http_client = http_client or HttpClient()

        self._v1 = None

    @property
    def v1(self):
        if not self._v1:
            self._v1 = V1(self)

        return self._v1

    def absolute_url(self, uri):
        return '{}{}'.format(self.API, uri)

    def request(self, method, url, params=None, data=None, headers=None):
        headers = headers or {}
        headers['Authorization'] = self.auth.auth_string

        if data and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'
            data = json.dumps(data)

        response = self.http_client.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers
        )

        response.raise_for_status()
        return response
