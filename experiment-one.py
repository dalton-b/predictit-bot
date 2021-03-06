from Classes.Database import Database
from Classes.NumberCruncher import NumberCruncher
from Classes.ExperimentOneDataObject import ExperimentOneDataObject
import matplotlib.pyplot as plt

database = Database()
number_cruncher = NumberCruncher(database.snapshots)
closed_markets = number_cruncher.get_markets_that_closed_on_end_date()

# Declare experiment outputs and parameters
percent_profit = []
num_num_data_points = []
days_to_check = 60

for day in range(0, days_to_check):

    data_objects = [ExperimentOneDataObject(x, y, day, database) for x, y in closed_markets.items()]
    agg_prices_close = 0.0
    agg_prices_pre_close = 0.0
    num_data_points = 0
    for data_object in data_objects:

        if data_object.price_pre_close is not None and data_object.price_close is not None:
            agg_prices_pre_close += data_object.price_pre_close
            agg_prices_close += data_object.price_close
            num_data_points += 1

    percent_profit.append(agg_prices_pre_close / agg_prices_close)
    num_num_data_points.append(num_data_points)

fig, ax = plt.subplots()
ax.plot(percent_profit)
ax.set_xlim(days_to_check, 0)
ax.set_title("Normalized Returns - Experiment 1")
ax.set_xlabel("Days to Market Close")
ax.set_ylabel("Normalized Returns")
plt.savefig("experiment-one/percent_profit_60_day.png")
plt.close()

with open('experiment-one/results.txt', 'w') as f:
    f.write("Average returns: " + str(sum(percent_profit) / len(percent_profit)))

fig, ax = plt.subplots()
ax.plot(num_num_data_points)
ax.set_xlim(days_to_check, 0)
ax.set_title("Number of Contracts Per Day Before Market Close")
ax.set_xlabel("Days to Market Close")
ax.set_ylabel("Number of Contracts")
plt.savefig("experiment-one/num_contracts.png")
