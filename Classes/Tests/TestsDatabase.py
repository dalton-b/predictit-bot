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
        for snapshot in database.snapshots:
            if len(snapshot.markets) < markets:
                markets = len(snapshot.markets)
        self.assertTrue(markets > 0)

    def test_markets_have_contracts(self):
        database = Database()
        contracts = math.inf
        for snapshot in database.snapshots:
            for market in snapshot.markets:
                if len(market.contracts) < contracts:
                    contracts = len(market.contracts)
        self.assertTrue(contracts > 0)


if __name__ == '__main__':
    unittest.main()
