class ExperimentOneDataObject(object):

    def __init__(self, market_id, close_date):
        self.market_id = market_id
        self.close_date = close_date
        self.contract_of_choice_id = None
        self.contract_option = None
        self.price_pre_close = None
        self.price_close = None

    def set_contract_of_choice_id(self, contract_id):
        self.contract_of_choice_id = contract_id

    def set_price_pre_close(self, price):
        self.price_pre_close = price

    def set_price_close(self, price):
        self.price_close = price

    def set_contract_option(self, option):
        self.contract_option = option


