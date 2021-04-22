from Classes.DataCollector import DataCollector
from Classes.Database import Database

data_collector = DataCollector()
data_collector.collect_data()
data_collector.export_content()

database = Database()

