from Classes.FileManager import FileManager
from datetime import datetime, timezone, timedelta

class HTMLWriter:

    def __init__(self):

        self._file_manager = FileManager()
        self._html_skeleton = """<!DOCTYPE html>
<html>
\t<body>
\t\t<div>
\t\t\t<h1>Hello world!</h1>
\t\t\t<p>This is my PredictIt project.</p>
\t\t\t<p>This page was last updated at UTC-5: """ + datetime.now(tz=timezone(timedelta(hours=-5))).strftime("%Y-%m-%d %H:%M:%S") + """
\t\t</div>
\t</body>
</html>"""

    def write(self, file_name):

        full_file_path = self.file_manager.combine_file_path_and_name(self.file_manager.root_dir, file_name)

        with open(full_file_path, "w") as html_file:
            html_file.write(self.html_skeleton)

    @property
    def file_manager(self):
        return self._file_manager

    @property
    def html_skeleton(self):
        return self._html_skeleton

    





