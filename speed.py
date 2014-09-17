class SpeedError(Exception):

    """Speed intialize exception"""


class Speed(float):

    def __new__(cls, *args, **kwargs):
        try:
            # return float.__new__(cls, *args, **kwargs)
            return super(Speed, cls).__new__(cls, *args, **kwargs)
        except(TypeError, ValueError):
            raise SpeedError("No way")

    @classmethod
    def from_mh(cls, mph):
        meters_per_second = mph / (1609.44/3600)
        return cls(meters_per_second)

    @classmethod
    def from_kmh(cls, kmh):
        meters_per_second = kmh * (5/18.0)
        return cls(meters_per_second)

    def _to_kmh(self):
        kmh = self * (18/5.0)
        return kmh

    def _to_mh(self):
        mph = self * 2.2369
        return mph

    @property
    def kmh(self):
        return self._to_kmh()

    @property
    def mph(self):
        return self._to_mh()

    @property
    def meters_per_second(self):
        return self
