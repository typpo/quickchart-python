from quickchart import QuickChart, QuickChartFunction

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
            "data": [1, 2],
            "backgroundColor": QuickChartFunction("getGradientFillHelper('vertical', ['rgba(63, 100, 249, 0.2)', 'rgba(255, 255, 255, 0.2)'])"),
        }]
    }
}

print(qc.get_url())
