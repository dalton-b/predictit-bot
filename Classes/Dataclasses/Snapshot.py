import json
from datetime import datetime
from Market import Market


class Snapshot:

    def __init__(self, file_name, file_contents):

        self._time = datetime.strptime(file_name[:-len(".txt")], "%Y-%m-%d-%H-%M-%S")
        self._markets = self.get_markets(file_contents)

    @staticmethod
    def get_markets(file_contents):
        markets_dict = json.loads(file_contents)['markets']
        markets = []
        for market_dict in markets_dict:
            markets.append(Market(market_dict))
        return markets

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
