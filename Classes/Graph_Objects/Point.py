class Point:

    def __init__(self, day, bias, num_data_points):
        self._day = day
        self._bias = bias
        self._num_data_points = num_data_points
        self._average_bias = bias / float(num_data_points)

    @property
    def average_bias(self):
        return self._average_bias

    @property
    def day(self):
        return self._day

    @property
    def bias(self):
        return self._bias

    @property
    def num_data_points(self):
        return self._num_data_points
