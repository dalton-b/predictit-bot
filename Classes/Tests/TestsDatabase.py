import math
import unittest
from Classes.Database import Database


class TestsDatabase(unittest.TestCase):

    def test_database_has_entries(self):
        database = Database()
        self.assertTrue(len(database.snapshots) > 0)

    def test_snapshots_have_markets(self):
        database = Database()
        markets = math.inf
        for data, snapshot in database.snapshots.items():
            if len(snapshot.markets) < markets:
                markets = len(snapshot.markets)
        self.assertTrue(markets > 0)

    def test_markets_have_contracts(self):
        database = Database()
        contracts = math.inf
        for time, snapshot in database.snapshots.items():
            for market in snapshot.markets:
                if len(market.contracts) < contracts:
                    contracts = len(market.contracts)
        self.assertTrue(contracts > 0)

    def test_one_contract_has_id(self):
        database = Database()
        snapshot = list(database.snapshots.values())[0]
        contract_id = snapshot.markets[0].get_contracts[0].id
        self.assertTrue(isinstance(contract_id, int))


if __name__ == '__main__':
    unittest.main()
