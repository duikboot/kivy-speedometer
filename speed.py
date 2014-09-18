class SpeedError(Exception):

    """Speed intialize exception"""


class Speed(float):

    """Speed type.

    Constructors:

    __new__()
    from_kph()
    from_mph()

    Properties (readonly):
    kph, mph, mps

    >>> kph = Speed.from_kph(30)
    >>> print "{:.2f}".format(kph)
    8.33
    >>> print "{:.2f}".format(kph.kph)
    30.00
    >>> print "{:.2f}".format(kph.mph)
    18.64
    """

    def __new__(cls, *args, **kwargs):
        try:
            # return float.__new__(cls, *args, **kwargs)
            return super(Speed, cls).__new__(cls, *args, **kwargs)
        except(TypeError, ValueError):
            raise SpeedError("No way")

    @classmethod
    def from_mph(cls, mph):
        """Construct speed from miles/hour."""
        mps = mph * 0.44704
        return cls(mps)

    @classmethod
    def from_kph(cls, kph):
        """Construct speed from kilometer/hour."""
        mps = kph * (5/18.0)
        return cls(mps)

    def _to_kph(self):
        kph = self * (18/5.0)
        return kph

    def _to_mph(self):
        mph = self * 2.2369
        return mph

    @property
    def kph(self):
        return self._to_kph()

    @property
    def mph(self):
        return self._to_mph()

    @property
    def mps(self):
        return self


if __name__ == '__main__':
    import doctest
    doctest.testmod()
