import csv
from datetime import datetime, timedelta

from Classes.Graph_Objects.Graph import Graph
from Classes.Graph_Objects.Point import Point
from Classes.FileManager import FileManager


class NumberCruncher:

    def __init__(self, snapshots):
        self._snapshots = snapshots
        self._lookback = 90
        self._graph = self.crunch_numbers()

    def crunch_numbers(self):

        closed_markets = self.get_closed_market_ids_and_dates()
        closed_contract_states = self.get_closed_contract_states(closed_markets)
        points = self.get_points(closed_contract_states)
        return Graph(points)

    def get_closed_market_ids_and_dates(self):
        closed_markets = {}
        snapshot_list = list(self._snapshots.values())
        for i in range(1, len(snapshot_list)):

            yesterday = snapshot_list[i-1]
            today = snapshot_list[i]

            yesterdays_market_ids = self.get_market_ids_from_snapshot(yesterday)
            todays_market_ids = self.get_market_ids_from_snapshot(today)

            closed_ids = self.get_closed_market_ids(yesterdays_market_ids, todays_market_ids)

            for market_id in closed_ids:
                closed_markets[market_id] = self.parse_market_date(yesterday.markets[0])

        return closed_markets

    @staticmethod
    def parse_market_date(market):
        return datetime.strptime(market.timeStamp.split("T")[0], "%Y-%m-%d").date()

    @staticmethod
    def get_closed_market_ids(yesterday_ids, today_ids):
        closed_ids = [x for x in yesterday_ids if x not in today_ids]
        return closed_ids

    def get_closed_contract_states(self, closed_markets):
        closed_contract_states = {}
        for closed_id, closed_date in closed_markets.items():
            contract_old_states = self.get_contract_old_states(closed_id, closed_date)
            closed_contract_states[closed_id] = contract_old_states

        return closed_contract_states

    def get_contract_old_states(self, closed_id, closed_date):
        contract_old_states = {}
        for i in range(0, self._lookback):
            past_date = closed_date - timedelta(days=i)
            contracts = self.get_contracts_from_market_id_and_date(closed_id, past_date)
            if contracts is not None:
                contract_old_states[i] = contracts
        return contract_old_states

    def get_points(self, closed_contract_states):
        points = []
        for i in range(0, self._lookback):
            bias = 0.0
            num_data_points = 0
            for key, contract_states in closed_contract_states.items():
                try:
                    num_contracts_at_state = len(contract_states[i])
                    for j in range(0, num_contracts_at_state):
                        final_state = contract_states[0][j]
                        past_state = contract_states[i][j]
                        bias += self.get_bias(final_state, past_state)
                        num_data_points += 1
                except KeyError:
                    pass
            if num_data_points != 0:
                points.append(Point(i, bias, num_data_points))
        return points

    @staticmethod
    def get_market_ids_from_snapshot(snapshot):
        ids = []
        for market in snapshot.markets:
            ids.append(market.id)
        return ids

    def get_contracts_from_market_id_and_date(self, market_id, market_date):
        try:
            for market in self._snapshots[market_date].markets:
                if market.id == market_id:
                    return market.contracts
        except KeyError:
            return None

    def get_bias(self, final_contract, current_contract):
        bias = 0
        final_yes = self.parse_contract(final_contract)
        current_yes = self.parse_contract(current_contract)
        bias += current_yes - final_yes
        return bias

    @staticmethod
    def parse_contract(contract):
        if contract.bestBuyYesCost is not None:
            return contract.bestBuyYesCost
        else:
            return contract.bestSellYesCost

    @property
    def snapshots(self):
        return self._snapshots

    @property
    def graph(self):
        return self._graph

    def write_bias_graph_to_csv(self, file_name):
        file_manager = FileManager()
        full_path = file_manager.combine_file_path_and_name(file_manager.output_dir, file_name)
        with open(full_path, 'w') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["day", "bias", "num_data_points", "average_bias"])
            for point in self.graph.points:
                csv_writer.writerow([point.day, point.bias, point.num_data_points, point.average_bias])

