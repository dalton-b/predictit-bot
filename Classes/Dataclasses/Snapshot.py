from datetime import datetime
import json

from Market import Market


class Snapshot:
    def __init__(self, file_name, file_contents):

        self._time = datetime.strptime(file_name[:-len(".txt")], "%Y-%m-%d-%H-%M-%S")
        markets_dict = json.loads(file_contents)['markets']
        markets = []
        for market_dict in markets_dict:
            markets.append(Market(market_dict))
        self._markets = markets

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
