import requests
import json
from network.base.base_requests import Tools


class BaseRequest:
    TIMEOUT_SEC = 300
    RETRY_TIMES = 3

    def __init__(self, url, cookie, additional_headers_dict, json=None):
        self.headers = Tools.build_headers(cookie, additional_headers_dict)
        self.url = url
        self.json = json
        self.response = None
        # print("url = " + self.url)
        # print("headers = " + str(self.headers))
        # print("TIMEOUT_SEC = " + str(self.TIMEOUT_SEC))

    def start(self):
        for i in range(self.RETRY_TIMES):
            try:
                self.response = self.start_request()
                return self.process_response()
            except Exception as e:
                print("Exception: fetch " + self.url + " got error = " + str(e))

    def start_request(self):
        if self.json is None:
            return requests.get(self.url, headers=self.headers, timeout=self.TIMEOUT_SEC)
        else:
            return requests.post(self.url, headers=self.headers, timeout=self.TIMEOUT_SEC, json=self.json)

    def process_response(self):
        return json.loads(self.response.content.decode("utf-8"))
