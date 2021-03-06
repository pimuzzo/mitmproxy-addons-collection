from mitmproxy import http, ctx

URL_TO_INTERCEPT = 'http://example.com/path'
MAX_NUMBER_OF_FAILS = 3
CORS_HEADER = 'http://localhost:3000'


class Simulate504:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        if flow.request.pretty_url == URL_TO_INTERCEPT and flow.request.method != 'OPTIONS':
            self.num = self.num + 1
            ctx.log.warn('Intercepted attempt number {} of {}'.format(self.num, MAX_NUMBER_OF_FAILS))
            if self.num <= MAX_NUMBER_OF_FAILS:
                flow.response = http.HTTPResponse.make(504, b'{}', {'Content-Type': 'application/json'})
                if CORS_HEADER:
                    flow.response.headers['Access-Control-Allow-Origin'] = CORS_HEADER
            else:
                self.num = 0  # reset


addons = [
    Simulate504()
]
