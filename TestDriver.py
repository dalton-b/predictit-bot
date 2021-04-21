import unittest
import TestsDataCollector


def run_data_collector_tests():
    suite = unittest.TestLoader().loadTestsFromModule(TestsDataCollector)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    run_data_collector_tests()
