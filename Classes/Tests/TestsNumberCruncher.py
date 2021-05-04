import unittest
from Classes.Database import Database
from Classes.Graph_Objects.Graph import Graph
from Classes.Graph_Objects.Point import Point
from Classes.NumberCruncher import NumberCruncher


class TestsNumberCruncher(unittest.TestCase):

    def test_initialize(self):
        database = Database()
        number_cruncher = NumberCruncher(database.snapshots)
        self.assertTrue(len(number_cruncher.snapshots) > 0)

    def test_graph_has_points(self):
        database = Database()
        number_cruncher = NumberCruncher(database.snapshots)
        graph = number_cruncher.graph
        points = graph.points
        self.assertTrue(len(points) > 0)


if __name__ == '__main__':
    unittest.main()