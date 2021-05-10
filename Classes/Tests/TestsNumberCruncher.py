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

    def test_resolve_to_no(self):
        database = Database("data_logs_tests/test_0")
        number_cruncher = NumberCruncher(database.snapshots)
        graph = number_cruncher.graph
        self.assertTrue(graph.points[1].average_bias == 0.5)

    def test_resolve_to_yes(self):
        database = Database("data_logs_tests/test_1")
        number_cruncher = NumberCruncher(database.snapshots)
        graph = number_cruncher.graph
        self.assertTrue(graph.points[1].average_bias == -0.5)

    def test_averages(self):
        database = Database("data_logs_tests/test_2")
        number_cruncher = NumberCruncher(database.snapshots)
        graph = number_cruncher.graph
        average_bias = graph.points[1].average_bias
        self.assertTrue(0.01 >= average_bias >= -0.01)


if __name__ == '__main__':
    unittest.main()