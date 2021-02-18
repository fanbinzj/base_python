from network.base.base_requests.BaseRequest import BaseRequest


class BaseJsonPostRequest(BaseRequest):

    def __init__(self, url, cookie, additional_headers_dict):
        super().__init__(url, cookie, additional_headers_dict, self.build_request_json())

    def build_request_json(self):
        pass
