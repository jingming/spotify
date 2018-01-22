from spotify.page import Page


class ArtistContext(object):

    def __init__(self, version, id):
        self.version = version
        self.id = id

    def fetch(self):
        response = self.version.request('GET', '/artists/{}'.format(self.id))
        return ArtistInstance(self.version, response.json())


class ArtistInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    def refresh(self):
        response = self.version.client.request('GET', self.href)
        self._properties = response.json()

    @property
    def external_urls(self):
        return self._properties['external_urls']

    @property
    def href(self):
        return self._properties['href']

    @property
    def id(self):
        return self._properties['id']

    @property
    def name(self):
        return self._properties['name']

    @property
    def type(self):
        return self._properties['type']

    @property
    def uri(self):
        return self._properties['uri']


class ArtistList(object):
    def __init__(self, version):
        self.version = version

    def get(self, id):
        return ArtistContext(self.version, id)

    def list(self, ids):
        response = self.version.request('GET', '/artists', params={
            'ids': ','.join(ids)
        })
        return ArtistPage(self.version, response.json(), 'artists')


class ArtistPage(Page):
    INSTANCE_CLASS = ArtistInstance
