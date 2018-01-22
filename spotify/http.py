import requests


class HttpClient(object):

    def get(self, url, params=None, headers=None, auth=None):
        return requests.get(url, params=params, headers=headers, auth=auth)

    def post(self, url, params=None, data=None, headers=None, auth=None):
        return requests.post(url, params=params, data=data, headers=headers, auth=auth)

    def put(self, url, params=None, data=None, headers=None, auth=None):
        return requests.put(url, params=params, data=data, headers=headers, auth=auth)

    def request(self, method, url, params=None, data=None, headers=None, auth=None):
        return requests.request(method, url, params=params, data=data, headers=headers, auth=auth)
