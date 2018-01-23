

class Bar(object):

    def __init__(self, start, duration, confidence):
        self.start = start
        self.duration = duration
        self.confidence = confidence

    @classmethod
    def from_json(cls, json):
        return Bar(
            json['start'],
            json['duration'],
            json['confidence']
        )


class Beat(object):

    def __init__(self, start, duration, confidence):
        self.start = start
        self.duration = duration
        self.confidence = confidence

    @classmethod
    def from_json(cls, json):
        return Beat(
            json['start'],
            json['duration'],
            json['confidence']
        )


class Meta(object):

    def __init__(self, analyzer_version, platform, detailed_status, status_code, timestamp,
                 analysis_time, input_process):
        self.analyzer_version = analyzer_version
        self.platform = platform
        self.detailed_status = detailed_status
        self.status_code = status_code
        self.timestamp = timestamp
        self.analysis_time = analysis_time
        self.input_process = input_process

    @classmethod
    def from_json(cls, json):
        return Meta(
            json['analyzer_version'],
            json['platform'],
            json['detailed_status'],
            json['status_code'],
            json['timestamp'],
            json['analysis_time'],
            json['input_process']
        )


class Section(object):

    def __init__(self, start, duration, confidence, loudness, tempo, tempo_confidence,
                 key, key_confidence, mode, mode_confidence, time_signature, time_signature_confidence):
        self.start = start
        self.duration = duration
        self.confidence = confidence
        self.loudness = loudness
        self.tempo = tempo
        self.tempo_confidence = tempo_confidence
        self.key = key
        self.key_confidence = key_confidence
        self.mode = mode
        self.mode_confidence = mode_confidence
        self.time_signature = time_signature
        self.time_signature_confidence = time_signature_confidence

    @classmethod
    def from_json(cls, json):
        return Section(
            json['start'],
            json['duration'],
            json['confidence'],
            json['loudness'],
            json['tempo'],
            json['tempo_confidence'],
            json['key'],
            json['key_confidence'],
            json['mode'],
            json['mode_confidence'],
            json['time_signature'],
            json['time_signature_confidence']
        )


class Segment(object):

    def __init__(self, start, duration, confidence, loudness_start, loudness_max_time, loudness_max,
                 loudness_end, pitches, timbre):
        self.start = start
        self.duration = duration
        self.confidence = confidence
        self.loudness_start = loudness_start
        self.loudness_max_time = loudness_max_time
        self.loudness_max = loudness_max
        self.loudness_end = loudness_end
        self.pitches = pitches
        self.timbre = timbre

    @classmethod
    def from_json(cls, json):
        return Segment(
            json['start'],
            json['duration'],
            json['confidence'],
            json['loudness_start'],
            json['loudness_max_time'],
            json['loudness_max'],
            json['loudness_end'],
            json['pitches'],
            json['timbre']
        )


class Tatum(object):

    def __init__(self, start, duration, confidence):
        self.start = start
        self.duration = duration
        self.confidence = confidence

    @classmethod
    def from_json(cls, json):
        return Tatum(
            json['start'],
            json['duration'],
            json['confidence']
        )


class Track(object):

    def __init__(self, num_samples, duration, sample_md5, offset_seconds, window_seconds, analysis_sample_rate,
                 analysis_channels, end_of_fade_in, start_of_fade_out, loudness, tempo, tempo_confidence,
                 time_signature, time_signature_confidence, key, key_confidence, mode, mode_confidence,
                 codestring, code_version, echoprintstring, echoprint_version, synchstring, synch_version,
                 rhythmstring, rhythm_version):
        self.num_samples = num_samples
        self.duration = duration
        self.sample_md5 = sample_md5
        self.offset_seconds = offset_seconds
        self.window_seconds = window_seconds
        self.analysis_sample_rate = analysis_sample_rate
        self.analysis_channels = analysis_channels
        self.end_of_fade_in = end_of_fade_in
        self.start_of_fade_out = start_of_fade_out
        self.loudness = loudness
        self.tempo = tempo
        self.tempo_confidence = tempo_confidence
        self.time_signature = time_signature
        self.time_signature_confidence = time_signature_confidence
        self.key = key
        self.key_confidence = key_confidence
        self.mode = mode
        self.mode_confidence = mode_confidence
        self.codestring = codestring
        self.code_version = code_version
        self.echoprintstring = echoprintstring
        self.echoprint_version = echoprint_version
        self.synchstring = synchstring
        self.synch_version = synch_version
        self.rhythmstring = rhythmstring
        self.rhythm_version = rhythm_version

    @classmethod
    def from_json(cls, json):
        return Track(
            json['num_samples'],
            json['duration'],
            json['sample_md5'],
            json['offset_seconds'],
            json['window_seconds'],
            json['analysis_sample_rate'],
            json['analysis_channels'],
            json['end_of_fade_in'],
            json['start_of_fade_out'],
            json['loudness'],
            json['tempo'],
            json['tempo_confidence'],
            json['time_signature'],
            json['time_signature_confidence'],
            json['key'],
            json['key_confidence'],
            json['mode'],
            json['mode_confidence'],
            json['codestring'],
            json['code_version'],
            json['echoprintstring'],
            json['echoprint_version'],
            json['synchstring'],
            json['synch_version'],
            json['rhythmstring'],
            json['rhythm_version']
        )
