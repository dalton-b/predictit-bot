class NumberCruncher:

    def __init__(self, snapshots):
        self._snapshots = snapshots
        self._graph = self.crunch_numbers()

    def crunch_numbers(self):
        self._snapshots.sort(key=lambda x: x._time, reverse=False)
        closed_markets = {}
        for i in range(1, len(self._snapshots)):
            yesterdays_markets = self._snapshots[i-1].markets
            yesterdays_market_ids = []
            for market in yesterdays_markets:
                yesterdays_market_ids.append(market.id)
            todays_markets = self._snapshots[i].markets
            todays_market_ids = []
            for market in todays_markets:
                todays_market_ids.append(market.id)
            closed_markets[yesterdays_markets[0].timeStamp] = [x for x in yesterdays_market_ids if x not in todays_market_ids]
        return None

    @property
    def snapshots(self):
        return self._snapshots

    @property
    def graph(self):
        return self._graph
