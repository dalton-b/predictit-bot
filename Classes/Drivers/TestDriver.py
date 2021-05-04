import unittest
from Classes.Tests import TestsDataCollector, TestsDatabase, TestsHTMLWriter


def run_data_collector_tests():
    print("Running DataCollector tests...")
    suite = unittest.TestLoader().loadTestsFromModule(TestsDataCollector)
    unittest.TextTestRunner().run(suite)


def run_database_tests():
    print("Running Database tests...")
    suite = unittest.TestLoader().loadTestsFromModule(TestsDatabase)
    unittest.TextTestRunner().run(suite)


def run_html_writer_tests():
    print("Running HTMLWriter tests...")
    suite = unittest.TestLoader().loadTestsFromModule(TestsHTMLWriter)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    run_data_collector_tests()
    run_database_tests()
    run_html_writer_tests()
