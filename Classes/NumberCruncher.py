from datetime import datetime, timedelta


class NumberCruncher:

    def __init__(self, snapshots):
        self._snapshots = snapshots

        # Store snapshots in a dictionary accessible by date
        self._snapshots_by_date = {}
        for snapshot in self.snapshots:
            self._snapshots_by_date[snapshot.time.date()] = snapshot

        self._graph = self.crunch_numbers()



    def crunch_numbers(self):
        self._snapshots.sort(key=lambda x: x.time, reverse=False)
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
            closed_ids = [x for x in yesterdays_market_ids if x not in todays_market_ids]
            for id in closed_ids:
                closed_markets[id] = datetime.strptime(yesterdays_markets[0].timeStamp.split("T")[0], "%Y-%m-%d").date()



        # For each closed market
        closed_contracts = {}
        for closed_id, closed_date in closed_markets.items():
            contracts_lookback = {}
            for i in range(0, 90):
                delta = closed_date - timedelta(days=i)
                contracts = self.get_contracts_from_market_id_and_date(closed_id, delta)
                if contracts is not None:
                    contracts_lookback[i] = contracts
            closed_contracts[closed_id] = contracts_lookback

        day_bias = {}
        for i in range(0, 90):
            bias = 0.0
            bias_denominator = 0.0
            for key, contracts in closed_contracts.items():
                if key == 7221 and i == 6:
                    hi = 0

                try:
                    for j in range(0, len(contracts[i])):
                        bias += self.get_bias(contracts[0][j], contracts[i][j])
                        bias_denominator += 1.0
                except(KeyError):
                    pass
            if bias_denominator != 0.0:
                day_bias[i] = bias / bias_denominator

        # Store the bias for a given day in a date dictionary with keys 1-90, representing days before market close

        return None

    def get_contracts_from_market_id_and_date(self, market_id, market_date):

        try:
            for market in self._snapshots_by_date[market_date].markets:
                if market.id == market_id:
                    return market.contracts
        except(KeyError):
            return None

    def get_bias(self, final_contract, current_contract):
        bias = 0

        bias += (self.parse_cost(final_contract.bestBuyNoCost) - self.parse_cost(current_contract.bestBuyNoCost))
        bias += (self.parse_cost(final_contract.bestBuyYesCost) - self.parse_cost(current_contract.bestBuyYesCost))
        bias += (self.parse_cost(final_contract.bestSellNoCost) - self.parse_cost(current_contract.bestSellNoCost))
        bias += (self.parse_cost(final_contract.bestSellYesCost) - self.parse_cost(current_contract.bestSellYesCost))
        return bias

    @staticmethod
    def parse_cost(cost):
        if cost is not None:
            return cost
        else:
            return float(0.0)

    @property
    def snapshots(self):
        return self._snapshots

    @property
    def graph(self):
        return self._graph
