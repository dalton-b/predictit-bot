class Contract(object):

    def __init__(self, contract):

        self.set_attributes(contract)

    def set_attributes(self, contract):
        for key in contract:
            setattr(self, key, contract[key])
