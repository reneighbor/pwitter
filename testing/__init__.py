import base64
from service import app


class RequestsResponse(object):
    def __init__(self, resp):
        self._raw_resp = resp
        self.resp = resp
        self.status_code = resp.status_code
        self.headers = resp.headers
        self.text = resp.data
        self.content = resp.data


class LocalTestClient(object):
    def __init__(self, app):
        self.app = app


    def request(self, method, url, auth=None, **kwargs):
        headers = kwargs.get("headers", {})

        if auth:
            headers['Authorization'] = 'Basic ' + \
                                       base64.b64encode(auth[0] + ":" + auth[1])

        kwargs["headers"] = headers

        return RequestsResponse(self.app.open(url, method=method, **kwargs))

    def get(self, *args, **kw):
        return self.request("GET", *args, **kw)

    def post(self, *args, **kw):
        return self.request("POST", *args, **kw)

    def delete(self, *args, **kw):
        return self.request("DELETE", *args, **kw)


testing_client = LocalTestClient(app.test_client())
