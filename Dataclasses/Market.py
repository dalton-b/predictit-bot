from Contract import Contract


class Market(object):

    def __init__(self, market):
        for key in market:
            setattr(self, key, market[key])

        contracts = []

        for contract in self.contracts:
            contracts.append(Contract(contract))

        self.contracts = contracts
        pass