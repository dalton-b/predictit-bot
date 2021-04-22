class Contract(object):

    def __init__(self, contract):
        for key in contract:
            setattr(self, key, contract[key])
