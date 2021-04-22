import unittest
from Classes.DataCollector import DataCollector


class TestsDataCollector(unittest.TestCase):

    def test_error_code(self):
        data_collector = DataCollector()
        data_collector.collect_data()
        self.assertEqual(200, data_collector.status_code)

    def test_content_not_null(self):
        data_collector = DataCollector()
        data_collector.collect_data()
        self.assertIsNotNone(data_collector.response)


if __name__ == '__main__':
    unittest.main()
