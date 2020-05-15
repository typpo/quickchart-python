"""A python client for quickchart.io, a web service that generates static
charts."""

import json
try:
    from urllib import urlencode
except:
    # For Python 3
    from urllib.parse import urlencode

class QuickChart:
    def __init__(self):
        self.config = None
        self.width = 500
        self.height = 300
        self.background_color = '#ffffff'
        self.device_pixel_ratio = 1.0
        self.format = 'png'
        self.key = None

    def is_valid(self):
        return self.config is not None

    def get_url(self):
        if not self.is_valid():
            raise RuntimeError('You must set the `config` attribute before generating a url')
        params = {
            'c': json.dumps(self.config),
            'w': self.width,
            'h': self.height,
            'bkg': self.background_color,
            'devicePixelRatio': self.device_pixel_ratio,
            'f': self.format,
        }
        if self.key:
            params['key'] = self.key
        return 'https://quickchart.io/chart?%s' % urlencode(params)

    def get_short_url(self):
        try:
            import requests
        except:
            raise RuntimeError('Could not find `requests` dependency')

        postdata = {
            'chart': json.dumps(self.config),
            'width': self.width,
            'height': self.height,
            'backgroundColor': self.background_color,
            'devicePixelRatio': self.device_pixel_ratio,
            'format': self.format,
        }
        if self.key:
            postdata['key'] = self.key
        resp = requests.post('https://quickchart.io/chart/create', json=postdata)
        if resp.status_code != 200:
            raise RuntimeError('Invalid response code from chart creation endpoint')
        parsed = json.loads(resp.text)
        if not parsed['success']:
            raise RuntimeError('Failure response status from chart creation endpoint')
        return parsed['url']
