import os


class FileManager:

    def __init__(self):
        self._root_dir = self.get_root_directory()
        self._output_dir = self._root_dir + "/output"

    @property
    def root_dir(self):
        return self._root_dir

    @property
    def output_dir(self):
        return self._output_dir

    @staticmethod
    def get_root_directory():
        return os.path.dirname(os.path.dirname(__file__))

    @staticmethod
    def combine_file_path_and_name(file_path, file_name):
        # TODO: Detect OS and react appropriately
        return file_path + "/" + file_name

    def combine_root_dir_and_file_name(self, file_name):
        return self.combine_file_path_and_name(self.root_dir, file_name)
