import glob
import os


class Database:
    def __init__(self):

        self._file_list = {}

        os.chdir("data_logs")
        for file in glob.glob("*.txt"):
            with open(file, "r") as f:
                self._file_list[file] = f.read()
        pass
