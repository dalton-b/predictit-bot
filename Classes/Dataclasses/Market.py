from Classes.Dataclasses.Contract import Contract


class Market(object):

    def __init__(self, market):

        self.set_attributes(market)
        self.contracts = self.populate_contracts()

    def set_attributes(self, market):
        for key in market:
            setattr(self, key, market[key])

    def populate_contracts(self):
        contracts = []
        for contract in self.contracts:
            contracts.append(Contract(contract))
        return contracts

    @property
    def get_contracts(self):
        return self.contracts

    def contract_lookup(self, contract_id):
        for contract in self.contracts:
            if contract.id == contract_id:
                return contract
