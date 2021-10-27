class ExperimentTwoDataObject(object):

    def __init__(self, contract, date, threshold):
        self.contract_id = contract.id
        self.date = date
        self.type = "None"
        self.current_price = 0.0
        if contract.bestBuyNoCost is not None:
            if contract.bestBuyNoCost > threshold:
                self.current_price = contract.bestBuyNoCost
                self.type = "no"
        # if contract.bestSellNoCost is not None:
        #     if contract.bestSellNoCost > threshold:
        #         self.current_price = contract.bestSellNoCost
        #         self.type = "no"
        # if contract.bestSellYesCost is not None:
        #     if contract.bestSellYesCost > threshold:
        #         self.current_price = contract.bestSellYesCost
        #         self.type = "yes"
        if contract.bestBuyYesCost is not None:
            if contract.bestBuyYesCost > threshold:
                self.current_price = contract.bestBuyYesCost
                self.type = "yes"
        self.close_price = 0.0
        self.profit = 0.0

    def set_close_price(self, close_price):
        self.close_price = close_price
        self.profit = self.close_price - self.current_price
