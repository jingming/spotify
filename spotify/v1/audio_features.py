from spotify.page import Page
from spotify.resource import Instance, Resource


class AudioFeaturesInstance(Instance):

    @property
    def danceability(self):
        return self.property('danceability')

    @property
    def energy(self):
        return self.property('energy')

    @property
    def key(self):
        return self.property('key')

    @property
    def loudness(self):
        return self.property('loudness')

    @property
    def mode(self):
        return self.property('mode')

    @property
    def speechiness(self):
        return self.property('speechiness')

    @property
    def acousticness(self):
        return self.property('acousticness')

    @property
    def instrumentalness(self):
        return self.property('instrumentalness')

    @property
    def liveness(self):
        return self.property('liveness')

    @property
    def valence(self):
        return self.property('valence')

    @property
    def tempo(self):
        return self.property('tempo')

    @property
    def type(self):
        return self.property('type')

    @property
    def id(self):
        return self.property('id')

    @property
    def uri(self):
        return self.property('uri')

    @property
    def track_href(self):
        return self.property('track_href')

    @property
    def analysis_url(self):
        return self.property('analysis_url')

    @property
    def duration_ms(self):
        return self.property('duration_ms')

    @property
    def time_signature(self):
        return self.property('time_signature')


class AudioFeaturesContext(Resource):

    def __init__(self, version, id):
        super(AudioFeaturesContext, self).__init__(version)
        self.id = id

    def fetch(self):
        response = self.version.request('GET', '/audio-features/{}'.format(self.id))
        return AudioFeaturesInstance(self.version, response.json())


class AudioFeaturesList(Resource):

    def list(self, ids=None):
        params = {}
        if ids:
            params['ids'] = ','.join(ids)

        response = self.version.request('GET', '/audio-features', params=params)
        return AudioFeaturesPage(self.version, response.json(), 'audio_features')


class AudioFeaturesPage(Page):

    @property
    def instance_class(self):
        return AudioFeaturesInstance
