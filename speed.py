class Speed(object):

    def __init__(self, meters_per_second):
        self._meters_per_second = meters_per_second

    @classmethod
    def from_mh(cls, mph):
        meters_per_second = mph / (1609.44/3600)
        return cls(meters_per_second)

    @classmethod
    def from_kmh(cls, kmh):
        meters_per_second = kmh * (5/18.0)
        return cls(meters_per_second)

    def _to_kmh(self):
        kmh = self._meters_per_second * (18/5.0)
        return kmh

    def _to_mh(self):
        mph = self._meters_per_second * 2.2369
        return mph

    @property
    def kmh(self):
        return self._to_kmh()

    @property
    def mph(self):
        return self._to_mh()

    @property
    def meters_per_second(self):
        return self._meters_per_second
