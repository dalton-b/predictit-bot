from datetime import timedelta
from Classes.ExperimentTwoDataObject import ExperimentTwoDataObject
from Classes.Database import Database
from Classes.NumberCruncher import NumberCruncher
from Classes.ExperimentOneDataObject import ExperimentOneDataObject
import matplotlib.pyplot as plt

database = Database()
number_cruncher = NumberCruncher(database.snapshots)
closed_markets_dict = number_cruncher.get_markets_that_closed_on_end_date()
threshold = 0.89
viable_contracts_close = []
agg_profits = []
num_num_contracts = []
agg_percent_profits = []

lookback = 60

for day in range(0, lookback):
    agg_profit = 0.0
    agg_current_price = 0.0
    agg_close_price = 0.0
    num_contracts = 0
    for closed_market_id, closed_market_date in closed_markets_dict.items():
        proceed = True
        lookback_date = closed_market_date - timedelta(days=day)
        try:
            closed_market_pre_close = number_cruncher.market_lookup(closed_market_id, lookback_date)
        except KeyError:
            proceed = False
        if closed_market_pre_close is None:
            proceed = False
        if proceed:
            for contract in closed_market_pre_close.contracts:
                if contract.has_price_above_threshold(threshold):
                    data_object = ExperimentTwoDataObject(contract, lookback_date, threshold)

                    closed_market = number_cruncher.market_lookup(closed_market_id, closed_market_date)
                    closed_contract = closed_market.contract_lookup(data_object.contract_id)
                    if data_object.type == "yes":
                        if closed_contract.bestSellYesCost is not None:
                            data_object.set_close_price(closed_contract.bestSellYesCost)
                        # if closed_contract.bestBuyYesCost is not None:
                        #     data_object.set_close_price(closed_contract.bestBuyYesCost)
                    if data_object.type == "no":
                        if closed_contract.bestSellNoCost is not None:
                            data_object.set_close_price(closed_contract.bestSellNoCost)
                        # if closed_contract.bestBuyNoCost is not None:
                        #     data_object.set_close_price(closed_contract.bestBuyNoCost)
                    agg_profit += data_object.profit
                    agg_current_price += data_object.current_price
                    agg_close_price += data_object.close_price
                    num_contracts += 1
    agg_profits.append(agg_profit)
    agg_percent_profits.append(agg_close_price / agg_current_price)
    num_num_contracts.append(num_contracts)

fig, ax = plt.subplots()
ax.plot(agg_percent_profits)
ax.set_xlim(lookback, 0)
ax.set_title("Percent Profits with $" + str(threshold) + " Threshold - Experiment 2")
ax.set_xlabel("Days to Market Close")
ax.set_ylabel("Percent Profits")
plt.savefig("experiment-two/pct_profit_60_day.png")
plt.close()

with open('experiment-two/results.txt', 'w') as f:
    f.write("Average profit: " + str(sum(agg_profits) / len(agg_profits)))

fig, ax = plt.subplots()
ax.plot(num_num_contracts)
ax.set_xlim(lookback, 0)
ax.set_title("Number of Contracts Per Day Before Market Close")
ax.set_xlabel("Days to Market Close")
ax.set_ylabel("Number of Contracts")
plt.savefig("experiment-two/num_contracts.png")

