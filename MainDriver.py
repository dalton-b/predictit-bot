from Classes.Database import Database
from Classes.HTMLWriter import HTMLWriter
from Classes.DataCollector import DataCollector


data_collector = DataCollector()
data_collector.collect_data()
data_collector.export_content()

database = Database()
# TODO: Create a NumberCruncher that takes a database and outputs a dictionary that the htmlwriter uses to write
html_writer = HTMLWriter()
html_writer.write("predictit-forecasting.html")
print("MainDriver run complete!")
