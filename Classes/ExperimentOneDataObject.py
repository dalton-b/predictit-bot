from datetime import timedelta


class ExperimentOneDataObject(object):

    def __init__(self, market_id, close_date, days_before_close, database):
        # self.number_cruncher = number_cruncher
        self.database = database
        self.market_id = market_id
        self.close_date = close_date
        self.days_before_close = days_before_close
        self.contract_of_choice_id, self.price_pre_close, self.contract_option = self.get_best_contract_info(
            self.market_id, self.close_date, self.days_before_close)

        self.price_close = self.get_previous_price(self.market_id, self.contract_of_choice_id, self.close_date, self.contract_option, 0)

    def set_contract_of_choice_id(self, contract_id):
        self.contract_of_choice_id = contract_id

    def set_price_pre_close(self, price):
        self.price_pre_close = price

    def set_price_close(self, price):
        self.price_close = price

    def set_contract_option(self, option):
        self.contract_option = option

    def get_best_contract_info(self, market_id, date, lookback):
        lookback_date = date - timedelta(days=lookback)
        try:
            market = self.database.market_lookup(market_id, lookback_date)
        except KeyError:
            return None, None, None
        if market is None:
            return None, None, None
        contracts = market.get_contracts
        price = 0.0
        type = ""
        contract_id = 0
        for contract in contracts:
            if contract.bestBuyYesCost is not None:
                if contract.bestBuyYesCost > price:
                    price = contract.bestBuyYesCost
                    type = "yes"
                    contract_id = contract.id
            if contract.bestSellYesCost is not None:
                if contract.bestSellYesCost > price:
                    price = contract.bestSellYesCost
                    type = "yes"
                    contract_id = contract.id
            if contract.bestBuyNoCost is not None:
                if contract.bestBuyNoCost > price:
                    price = contract.bestBuyNoCost
                    type = "no"
                    contract_id = contract.id
            if contract.bestSellNoCost is not None:
                if contract.bestSellNoCost > price:
                    price = contract.bestSellNoCost
                    type = "no"
                    contract_id = contract.id

        return contract_id, price, type

    def get_previous_price(self, market_id, contract_id, close_date, contract_option, lookback):
        lookback_date = close_date - timedelta(days=lookback)
        try:
            market = self.database.market_lookup(market_id, lookback_date)
        except KeyError:
            return None
        if market is None:
            return None
        contract = market.contract_lookup(contract_id)
        if contract_option == "no":
            if contract.bestBuyNoCost is not None:
                return contract.bestBuyNoCost
            else:
                return contract.bestSellNoCost
        elif contract_option == "yes":
            if contract.bestBuyYesCost is not None:
                return contract.bestBuyYesCost
            else:
                return contract.bestSellYesCost


