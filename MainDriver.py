from DataCollector import DataCollector
from Database import Database
from Parser import Parser
from Snapshot import Snapshot

data_collector = DataCollector()
data_collector.collect_data()
data_collector.export_content()

# database = Database()
# parser = Parser()
# snapshots = parser.parse_database(database)
