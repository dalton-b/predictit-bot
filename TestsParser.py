import unittest

from DataCollector import DataCollector
from Parser import Parser
from Database import Database


class TestsParser(unittest.TestCase):

    def test_0(self):

        database = Database()
        parser = Parser()
        snapshot = parser.parse_database(database)

        self.assertEqual(0, 1)


if __name__ == '__main__':
    unittest.main()
