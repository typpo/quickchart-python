import unittest
from datetime import datetime

from quickchart import QuickChart, QuickChartFunction

class TestQuickChart(unittest.TestCase):
    def test_simple(self):
        qc = QuickChart()
        qc.width = 600
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "bar",
            "data": {
                "labels": ["Hello world", "Test"],
                "datasets": [{
                    "label": "Foo",
                    "data": [1, 2]
                }]
            }
        }

        url = qc.get_url()
        self.assertIn('w=600', url)
        self.assertIn('h=300', url)
        self.assertIn('devicePixelRatio=2', url)
        self.assertIn('Hello+world', url)

    def test_no_chart(self):
        qc = QuickChart()
        qc.width = 600
        qc.height = 300
        qc.device_pixel_ratio = 2.0

        self.assertRaises(RuntimeError, qc.get_url)

    def test_get_bytes(self):
        qc = QuickChart()
        qc.width = 600
        qc.height = 300
        qc.config = {
            "type": "bar",
            "data": {
                "labels": ["Hello world", "Test"],
                "datasets": [{
                    "label": "Foo",
                    "data": [1, 2]
                }]
            }
        }
        self.assertTrue(len(qc.get_bytes()) > 8000)

    def test_with_function_and_dates(self):
        qc = QuickChart()
        qc.config = {
          "type": "bar",
          "data": {
            "labels": [datetime(2020, 1, 15), datetime(2021, 1, 15)],
            "datasets": [{
              "label": "Foo",
              "data": [1, 2]
            }]
          },
          "options": {
            "scales": {
              "yAxes": [{
                "ticks": {
                  "callback": QuickChartFunction('(val) => val + "k"')
                }
              }],
              "xAxes": [{
                "ticks": {
                  "callback": QuickChartFunction('(val) => "$" + val')
                }
              }]
            }
          }
        }

        url = qc.get_url()
        self.assertIn('7B%22ticks%22%3A%7B%22callback%22%3A%28val%29+%3D%3E+%22%24%22+%2B+val%7D%7D%5D%7D%7D%7D', url)
        self.assertIn('2020-01-15T00%3A00%3A00', url)

if __name__ == '__main__':
    unittest.main()
