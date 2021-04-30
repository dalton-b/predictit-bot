from Classes.HTMLWriter import HTMLWriter
import unittest


class TestsHTMLWriter(unittest.TestCase):

    def test_0(self):
        html_writer = HTMLWriter()
        html_writer.write_html("predictit-forecasting.html")
        self.assertTrue(0, 1)


if __name__ == '__main__':
    unittest.main()
