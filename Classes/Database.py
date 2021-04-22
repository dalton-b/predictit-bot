import glob
import os

from Snapshot import Snapshot


class Database:

    def __init__(self):

        self._file_list = {}
        self._root = os.path.dirname(os.path.dirname(__file__))
        self._directory = "data_logs"

        for file in os.listdir(self._root + "/" + self._directory):
            if file.endswith(".txt"):
                with open(self._root + "/" + self._directory + "/" + file, "r") as f:
                    self._file_list[file] = f.read()

        self._snapshots = []

        for file_name, file_contents in self.file_list.items():
            self._snapshots.append(Snapshot(file_name, file_contents))

    @property
    def file_list(self):
        return self._file_list

    @property
    def snapshots(self):
        return self._snapshots

    @property
    def directory(self):
        return self._directory
