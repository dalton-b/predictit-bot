from Classes.Database import Database
from Classes.NumberCruncher import NumberCruncher

database = Database()
number_cruncher = NumberCruncher(database.snapshots)
closed_markets = number_cruncher.get_markets_that_closed_on_end_date()

pass