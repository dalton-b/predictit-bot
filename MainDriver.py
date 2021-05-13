from Classes.Database import Database
from Classes.HTMLWriter import HTMLWriter
from Classes.DataCollector import DataCollector
from Classes.NumberCruncher import NumberCruncher


data_collector = DataCollector()
data_collector.collect_data()
data_collector.export_content()

database = Database()
number_cruncher = NumberCruncher(database.snapshots)
number_cruncher.write_bias_graph_to_csv("bias_graph.csv")
html_writer = HTMLWriter()
html_writer.write("predictit-forecasting.html")
print("MainDriver run complete!")
