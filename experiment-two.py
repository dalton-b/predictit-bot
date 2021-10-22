from Classes.Database import Database
from Classes.NumberCruncher import NumberCruncher
from Classes.ExperimentOneDataObject import ExperimentOneDataObject
import matplotlib.pyplot as plt

database = Database()
number_cruncher = NumberCruncher(database.snapshots)
closed_markets = number_cruncher.get_markets_that_closed_on_end_date()
percent_profit = []
num_num_data_points = []
days_to_check = 60
threshold = 0.89

for day in range(0, days_to_check):
    data_objects = []

    agg_prices_close = 0.0
    agg_prices_pre_close = 0.0
    num_data_points = 0
    for data_object in data_objects:
        contract_of_choice_id, contract_of_choice_price, contract_option = number_cruncher.get_contracts_of_choice(data_object.market_id, data_object.close_date, day, threshold)

        # Need to create new data objects, add all the qualities, etc
        data_object.set_contract_of_choice_id(contract_of_choice_id)
        data_object.set_price_pre_close(contract_of_choice_price)
        data_object.set_contract_option(contract_option)

        price_close = number_cruncher.get_previous_price(data_object.market_id, data_object.contract_of_choice_id, data_object.close_date, data_object.contract_option, 0)
        data_object.set_price_close(price_close)

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
plt.savefig("experiment-two/percent_profit_60_day.png")
plt.close()

with open('experiment-two/results.txt', 'w') as f:
    f.write("Average returns: " + str(sum(percent_profit) / len(percent_profit)))

fig, ax = plt.subplots()
ax.plot(num_num_data_points)
ax.set_xlim(days_to_check, 0)
ax.set_title("Number of Contracts Per Day Before Market Close")
ax.set_xlabel("Days to Market Close")
ax.set_ylabel("Number of Contracts")
plt.savefig("experiment-two/num_contracts.png")
