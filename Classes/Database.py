import glob
import os

from Snapshot import Snapshot


class Database:

    def __init__(self):

        self._file_list = {}

        os.chdir("data_logs")
        for file in glob.glob("*.txt"):
            with open(file, "r") as f:
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
