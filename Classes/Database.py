import os
from Classes.Dataclasses.Snapshot import Snapshot


class Database:

    def __init__(self, data_log_directory="data_logs"):

        self._data_log_directory = data_log_directory
        # TODO: Make this use the FileManager
        self._root = self.get_root_directory()
        self._data_log_path = self.get_data_log_path()
        self._file_list = self.get_file_list()
        self._snapshots = self.get_snapshots()

    @staticmethod
    def get_root_directory():
        return os.path.dirname(os.path.dirname(__file__))

    # TODO: Make this use the FileManager too
    def get_data_log_path(self):
        return self._root + "/" + self._data_log_directory

    def get_file_list(self):
        file_list = {}
        for file in self.get_text_files_in_directory(self._data_log_path):
            full_file_path = self.get_full_file_path(self._data_log_path, file)
            with open(full_file_path, "r") as f:
                file_list[file] = f.read()
        return file_list

    @staticmethod
    def get_full_file_path(directory, file_name):
        return directory + "/" + file_name

    @staticmethod
    def get_text_files_in_directory(directory):
        files = []
        for file in os.listdir(directory):
            if file.endswith(".txt"):
                files.append(file)
        return files

    def get_snapshots(self):
        snapshots = []
        for file_name, file_contents in self.file_list.items():
            snapshots.append(Snapshot(file_name, file_contents))
        snapshots_by_date = self.sort_snapshots(snapshots)
        sorted_snapshots_by_date = {}
        for date in sorted(snapshots_by_date):
            sorted_snapshots_by_date[date] = snapshots_by_date[date]
        return sorted_snapshots_by_date

    @staticmethod
    def sort_snapshots(snapshots):
        snapshots_by_date = {}
        for snapshot in snapshots:
            snapshots_by_date[snapshot.time.date()] = snapshot
        return snapshots_by_date

    @property
    def file_list(self):
        return self._file_list

    @property
    def snapshots(self):
        return self._snapshots

    @property
    def data_log_directory(self):
        return self._data_log_directory

    @property
    def root(self):
        return self._root
