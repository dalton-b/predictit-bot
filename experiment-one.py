from Classes.Database import Database
from Classes.NumberCruncher import NumberCruncher
from Classes.ExperimentOneDataObject import ExperimentOneDataObject

database = Database()
number_cruncher = NumberCruncher(database.snapshots)
closed_markets = number_cruncher.get_markets_that_closed_on_end_date()
data_objects = [ExperimentOneDataObject(x, y) for x, y in closed_markets.items()]

agg_prices_close = 0.0
agg_prices_30 = 0.0

for data_object in data_objects:
    contract_of_choice_id, contract_of_choice_price, contract_option = number_cruncher.get_contract_of_choice(data_object.market_id, data_object.close_date, 30)
    data_object.set_contract_of_choice_id(contract_of_choice_id)
    data_object.set_price_30(contract_of_choice_price)
    data_object.set_contract_option(contract_option)

    price_close = number_cruncher.get_previous_price(data_object.market_id, data_object.contract_of_choice_id, data_object.close_date, data_object.contract_option, 0)
    data_object.set_price_close(price_close)

    if data_object.price_30 is not None and data_object.price_close is not None:
        agg_prices_30 += data_object.price_30
        agg_prices_close += data_object.price_close


print(agg_prices_close - agg_prices_30)
pass