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

lookback = 60

for day in range(0, lookback):

    if day > 10:
        hello = 0
    agg_profit = 0.0
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
                    pass
                    agg_profit += data_object.profit
                    num_contracts += 1
    agg_profits.append(agg_profit)
    num_num_contracts.append(num_contracts)

    pass
pass

