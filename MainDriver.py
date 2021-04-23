from Classes.Database import Database
from Classes.DataCollector import DataCollector


data_collector = DataCollector()
data_collector.collect_data()
data_collector.export_content()

database = Database()

