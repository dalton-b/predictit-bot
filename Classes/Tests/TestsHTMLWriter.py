from Classes.HTMLWriter import HTMLWriter
from Classes.FileManager import FileManager
import unittest
import os


class TestsHTMLWriter(unittest.TestCase):

    def test_file_created_read_deleted(self):
        file_name = "test.html"
        html_writer = HTMLWriter()
        html_writer.write(file_name)
        file_manager = FileManager()
        full_path = file_manager.combine_root_dir_and_file_name(file_name)
        with open(full_path) as file:
            data = file.read()
        os.remove(full_path)
        self.assertFalse(os.path.exists(full_path))


if __name__ == '__main__':
    unittest.main()
