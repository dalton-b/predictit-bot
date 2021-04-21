from Parser import Parser


class Snapshot:
    def __init__(self):

        self._time = None
        self._markets = None

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time = time

    @property
    def markets(self):
        return self._markets

    @markets.setter
    def markets(self, markets):
        self._markets = markets
