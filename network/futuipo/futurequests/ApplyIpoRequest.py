from network.base.base_requests.BaseJsonPostRequest import BaseJsonPostRequest
import time

additional_headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Host": "ipo.futuhk.com"
}


def get_timestamp_and_random_id():
    request_id = str(time.time()).replace(".", "")[0:14]
    print("getTimeStampAndRandomId(): request_id = " + request_id)
    return request_id


class ApplyIpoRequest(BaseJsonPostRequest):
    url = "https://ipo.futuhk.com/api/applyStock?request_id="
    request_data = None

    def __init__(self, user, stock):
        self.user = user
        self.stock = stock
        super().__init__(self.url + get_timestamp_and_random_id(), user.cookie, additional_headers)

    def build_request_json(self):
        if self.request_data is None:
            self.request_data = self.stock.generate_request_data(self.user.apply_lots)
            self.request_data["accountId"] = self.user.account_id
            self.request_data["password"] = self.user.password
            self.request_data["r_token"] = self.user.r_token
            self.request_data["csrf"] = self.user.csrf

        print("request data = " + str(self.request_data))
        return self.request_data
