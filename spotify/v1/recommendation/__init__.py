from spotify import values
from spotify.object.seed import Seed
from spotify.resource import Resource, Instance
from spotify.v1.recommendation.available_genre_seeds import AvailableGenreSeedsContext


class Attributes(object):

    def __init__(self, acousticness=values.UNSET, danceability=values.UNSET, duration_ms=values.UNSET,
                 energy=values.UNSET, instrumentalness=values.UNSET, key=values.UNSET, liveness=values.UNSET,
                 loudness=values.UNSET, mode=values.UNSET, popularity=values.UNSET, speechiness=values.UNSET,
                 tempo=values.UNSET, time_signature=values.UNSET, valence=values.UNSET):
        self.acousticness = acousticness
        self.danceability = danceability
        self.duration_ms = duration_ms
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.key = key
        self.liveness = liveness
        self.loudness = loudness
        self.mode = mode
        self.popularity = popularity
        self.speechiness = speechiness
        self.tempo = tempo
        self.time_signature = time_signature
        self.valence = valence

    def payload(self, prefix):
        payload = values.of({
            'acousticness': self.acousticness,
            'danceability': self.danceability,
            'duration_ms': self.duration_ms,
            'energy': self.energy,
            'instrumentalness': self.instrumentalness,
            'key': self.key,
            'liveness': self.liveness,
            'loudness': self.loudness,
            'mode': self.mode,
            'popularity': self.popularity,
            'speechiness': self.speechiness,
            'tempo': self.tempo,
            'time_signature': self.time_signature,
            'valence': self.valence
        })
        payload = {'{}_{}'.format(prefix, k): v for k, v in payload.items()}
        return payload


class RecommendationInstance(Instance):

    def __init__(self, version, properties):
        super(RecommendationInstance, self).__init__(version, properties)
        self._context = RecommendationContext(self.version)

    @property
    def seeds(self):
        return [Seed.from_json(seed) for seed in self.property('seeds')]

    @property
    def tracks(self):
        from spotify.v1.track import TrackInstance
        return [TrackInstance(self.version, track) for track in self.property('tracks')]

    @property
    def available_genre_seeds(self):
        return self._context.available_genre_seeds


class RecommendationContext(Resource):

    def __init__(self, version):
        super(RecommendationContext, self).__init__(version)

        self._available_genre_seeds = None

    @property
    def available_genre_seeds(self):
        if not self._available_genre_seeds:
            self._available_genre_seeds = AvailableGenreSeedsContext(self.version)

        return self._available_genre_seeds

    def fetch(self, limit=values.UNSET, market=values.UNSET, seed_artists=None, seed_genres=None, seed_tracks=None,
              max_attributes=None, min_attributes=None, target_attributes=None):
        params = values.of({
            'limit': limit,
            'market': market
        })
        params.update(max_attributes.payload('max'))
        params.update(min_attributes.payload('min'))
        params.update(target_attributes.payload('target'))

        if seed_artists:
            params['seed_artists'] = ','.join(seed_artists)
        if seed_genres:
            params['seed_genres'] = ','.join(seed_genres)
        if seed_tracks:
            params['seed_tracks'] = ','.join(seed_tracks)

        response = self.version.request('GET', '/recommendations', params=params)
        return RecommendationInstance(self.version, response.json())
