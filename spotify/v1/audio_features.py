from spotify import values
from spotify.page import Page


class AudioFeaturesInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def danceability(self):
        return self._properties['danceability']

    @property
    def energy(self):
        return self._properties['energy']

    @property
    def key(self):
        return self._properties['key']

    @property
    def loudness(self):
        return self._properties['loudness']

    @property
    def mode(self):
        return self._properties['mode']

    @property
    def speechiness(self):
        return self._properties['speechiness']

    @property
    def acousticness(self):
        return self._properties['acousticness']

    @property
    def instrumentalness(self):
        return self._properties['instrumentalness']

    @property
    def liveness(self):
        return self._properties['liveness']

    @property
    def valence(self):
        return self._properties['valence']

    @property
    def tempo(self):
        return self._properties['tempo']

    @property
    def type(self):
        return self._properties['type']

    @property
    def id(self):
        return self._properties['id']

    @property
    def uri(self):
        return self._properties['uri']

    @property
    def track_href(self):
        return self._properties['track_href']

    @property
    def analysis_url(self):
        return self._properties['analysis_url']

    @property
    def duration_ms(self):
        return self._properties['duration_ms']

    @property
    def time_signature(self):
        return self._properties['time_signature']


class AudioFeaturesContext(object):

    def __init__(self, version, id):
        self.version = version
        self.id = id

    def fetch(self):
        response = self.version.request('GET', '/audio-features/{}'.format(self.id))
        return AudioFeaturesInstance(self.version, response.json())


class AudioFeaturesList(object):

    def __init__(self, version):
        self.version = version

    def list(self, ids=values.UNSET):
        params = values.of({
            'ids': ','.join(ids)
        })
        response = self.version.request('GET', '/audio-features', params=params)
        return AudioFeaturesPage(self.version, response.json(), 'audio_features')


class AudioFeaturesPage(Page):

    @property
    def instance_class(self):
        return AudioFeaturesInstance
