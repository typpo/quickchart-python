from quickchart import QuickChart

qc = QuickChart()
qc.config = {
    "type": "bar",
    "data": {
        "labels": ["Hello world", "Test"],
        "datasets": [{
            "label": "Foo",
            # Count from 0 to 100
            "data": list(range(0, 100)),
        }]
    }
}

print(qc.get_short_url())
#
# Example output (note that this shortened URL is now expired and will not display a chart):
#
# https://quickchart.io/chart/render/f-b4bf9221-0499-4bc6-b1ae-6f7c78be9d93
#
