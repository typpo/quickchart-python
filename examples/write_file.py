from quickchart import QuickChart

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

qc.to_file('/tmp/mychart.png')

print('Done.')
