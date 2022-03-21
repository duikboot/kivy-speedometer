class SpeedError(Exception):

    """Speed intialize exception"""


class Speed:

    """Speed type.

    Constructors:

    from_kph()
    from_mph()

    Properties readonly:
    kph, mph, meter_per_second

    >>> speed = Speed()
    >>> print(speed)
    Speed: 0.00 meter_per_second
    >>> speed.kph = 30
    >>> print(speed)
    Speed: 8.33 meter_per_second
    >>> null = Speed()
    >>> print(f"{null:.2f}")
    0.00
    >>> print(null.kph, null.mph, null.meter_per_second)
    0.0 0.0 0.0
    >>> kph = Speed.from_kph(30)
    >>> print(kph)
    Speed: 8.33 meter_per_second
    >>> print(f"{kph:.2f}")
    8.33
    >>> print(f"{kph.kph:.2f}")
    30.00
    >>> print(f"{kph.mph:.2f}")
    18.64
    >>> print(f"{kph.meter_per_second:.2f}")
    8.33
    >>> print(f"{kph:.2f}")
    8.33
    >>> print(f"{kph.kph:.2f}")
    30.00
    """

    def __init__(self, meter_per_second=0.0):
        self._meter_per_second = meter_per_second

    @classmethod
    def from_mph(cls, mph):
        """Construct speed from miles/hour."""
        meter_per_second = cls._meter_per_second_from_mph(mph)
        return cls(meter_per_second)

    @classmethod
    def from_kph(cls, kph):
        """Construct speed from kilometer/hour."""
        meter_per_second = cls._meter_per_second_from_kph(kph)
        return cls(meter_per_second=meter_per_second)

    def __str__(self):
        return f'Speed: {self._meter_per_second:.2f} meter_per_second'

    def __format__(self, format_spec):
        return format(self._meter_per_second, format_spec)

    @staticmethod
    def _meter_per_second_from_kph(kph):
        meter_per_second = kph * (5/18.0)
        return meter_per_second

    @staticmethod
    def _meter_per_second_from_mph(mph):
        meter_per_second = mph * 0.44704
        return meter_per_second

    def _to_kph(self):
        kph = self._meter_per_second * (18/5.0)
        return kph

    def _to_mph(self):
        mph = self._meter_per_second * 2.2369
        return mph

    @property
    def kph(self):
        return self._to_kph()

    @kph.setter
    def kph(self, value):
        self._meter_per_second = self._meter_per_second_from_kph(value)

    @property
    def mph(self):
        return self._to_mph()

    @mph.setter
    def mph(self, mph):
        self._meter_per_second = self._meter_per_second_from_mph(mph)

    @property
    def meter_per_second(self):
        return float(self._meter_per_second)

    @meter_per_second.setter
    def meter_per_second(self, meter_per_second):
        self.meter_per_second = self._meter_per_second


if __name__ == '__main__':
    import doctest
    doctest.testmod()
