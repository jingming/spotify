from spotify.object.audio_analysis import Bar, Beat, Meta, Section, Segment, Tatum, Track


class AudioAnalysisInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties

    @property
    def bars(self):
        return [Bar.from_json(bar) for bar in self._properties['bars']]

    @property
    def beats(self):
        return [Beat.from_json(beat) for beat in self._properties['beats']]

    @property
    def meta(self):
        return Meta.from_json(self._properties['meta'])

    @property
    def sections(self):
        return [Section.from_json(section) for section in self._properties['sections']]

    @property
    def segments(self):
        return [Segment.from_json(segment) for segment in self._properties['segments']]

    @property
    def tatums(self):
        return [Tatum.from_json(tatum) for tatum in self._properties['tatum']]

    @property
    def track(self):
        return Track.from_json(self._properties['track'])


class AudioAnalysisContext(object):

    def __init__(self, version, id):
        self.version = version
        self.id = id

    def fetch(self):
        response = self.version.request('GET', '/audio-analysis/{}'.format(self.id))
        return AudioAnalysisInstance(self.version, response.json())


class AudioAnalysisList(object):

    def __init__(self, version):
        self.version = version

    def get(self, id):
        return AudioAnalysisContext(self.version, id)
