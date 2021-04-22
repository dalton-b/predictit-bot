import unittest

from Classes.Database import Database
from Classes.Dataclasses.Snapshot import Snapshot


class TestsDatabase(unittest.TestCase):

    def test_0(self):

        database = Database()


        self.assertEqual(0, 1)


if __name__ == '__main__':
    unittest.main()
