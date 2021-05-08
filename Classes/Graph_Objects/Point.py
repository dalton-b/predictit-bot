class Point:

    def __init__(self, day, bias, num_data_points):
        self._day = day
        self._bias = bias
        self._num_data_points = num_data_points
        self._average_bias = bias / num_data_points

    @property
    def average_bias(self):
        return self._average_bias
