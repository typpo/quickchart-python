from datetime import datetime

from quickchart import QuickChart, QuickChartFunction

qc = QuickChart()
qc.width = 600
qc.height = 300
qc.device_pixel_ratio = 2.0
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
            }, {
                "ticks": {
                    "callback": QuickChartFunction('''function(val) {
                      return val + '???';
                    }''')
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

print(qc.get_url())
