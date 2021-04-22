import requests
from datetime import datetime
import json


class DataCollector:
    def __init__(self):
        self._endpoint = 'https://www.predictit.org/api/marketdata/all/'
        self._response = None
        self._status_code = None

    def collect_data(self):
        raw_response = requests.get(self._endpoint)
        self._response = raw_response.json()
        self._status_code = raw_response.status_code

    def export_content(self):
        current_time = get_current_time()
        data_filepath = create_data_filepath(current_time)

        with open(data_filepath, "w") as text_file:
            json.dump(self.response, text_file)

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, response):
        self._response = response

    @property
    def status_code(self):
        return self._status_code


def get_current_time():
    current_time = datetime.now()
    current_time_string = current_time.strftime("%Y-%m-%d-%H-%M-%S")
    return current_time_string


def create_data_filepath(current_time):
    full_filepath = "data_logs/" + current_time + ".txt"
    return full_filepath
