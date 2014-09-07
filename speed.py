class Speed(object):

    def __init__(self, ms):
        self._ms = ms

    @classmethod
    def from_mh(cls, mh):
        ms = mh / (1609.44/3600)
        return cls(mh)

    @classmethod
    def from_kmh(cls, kmh):
        ms = kmh * (5/18.0)
        return cls(ms)

    def _to_kmh(self):
        kmh = self._ms * (18/5.0)
        return kmh

    def _to_mh(self):
        mh = self._ms * 2.2369
        return mh

    @property
    def kmh(self):
        return self._to_kmh()

    @property
    def mh(self):
        return self._to_mh()

    @property
    def ms(self):
        return self._ms
