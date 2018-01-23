from spotify.object.audio_analysis import Bar, Beat, Meta, Section, Segment, Tatum, Track
from spotify.resource import Instance, Resource


class AudioAnalysisInstance(Instance):

    @property
    def bars(self):
        return [Bar.from_json(bar) for bar in self.property('bars')]

    @property
    def beats(self):
        return [Beat.from_json(beat) for beat in self.property('beats')]

    @property
    def meta(self):
        return Meta.from_json(self.property('meta'))

    @property
    def sections(self):
        return [Section.from_json(section) for section in self.property('sections')]

    @property
    def segments(self):
        return [Segment.from_json(segment) for segment in self.property('segments')]

    @property
    def tatums(self):
        return [Tatum.from_json(tatum) for tatum in self.property('tatum')]

    @property
    def track(self):
        return Track.from_json(self.property('track'))


class AudioAnalysisContext(Resource):

    def __init__(self, version, id):
        super(AudioAnalysisContext, self).__init__(version)
        self.id = id

    def fetch(self):
        response = self.version.request('GET', '/audio-analysis/{}'.format(self.id))
        return AudioAnalysisInstance(self.version, response.json())


class AudioAnalysisList(Resource):

    def get(self, id):
        return AudioAnalysisContext(self.version, id)
