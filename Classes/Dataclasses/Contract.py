class Contract(object):

    def __init__(self, contract):

        self.set_attributes(contract)

    def set_attributes(self, contract):
        for key in contract:
            setattr(self, key, contract[key])

    def has_price_above_threshold(self, threshold):
        if self.bestBuyYesCost is not None:
            if self.bestBuyYesCost > threshold:
                return True
        if self.bestSellYesCost is not None:
            if self.bestSellYesCost > threshold:
                return True
        if self.bestBuyNoCost is not None:
            if self.bestBuyNoCost > threshold:
                return True
        if self.bestSellNoCost is not None:
            if self.bestSellNoCost > threshold:
                return True

        return False
