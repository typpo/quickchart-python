import unittest

from quickchart import QuickChart

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

if __name__ == '__main__':
    unittest.main()
