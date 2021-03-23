from bs4 import BeautifulSoup
from network.base.base_requests.BaseHtmlGetRequest import BaseHtmlGetRequest
import time
import re

additional_headers = {
    "Content-Type": "text/html; charset=utf-8",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Host": "ipo.futuhk.com"
}


def get_timestamp_and_random_id():
    request_id = str(time.time()).replace(".", "")[0:14]
    print("getTimeStampAndRandomId(): request_id = " + request_id)
    return request_id


class ApplyDetailsRequest(BaseHtmlGetRequest):
    url = "https://ipo.futuhk.com/apply/detail?stockCode="

    def __init__(self, user, stock):
        self.user = user
        self.stock = stock
        super().__init__(self.url + stock.stockCode, user.cookie, additional_headers)

    def process_html_soup_result(self):
        try:
            target_script_string = self.soup(text=lambda t: "_params.csrf" in t)[0]
            csrf_str = re.search('_params.csrf = \'(.+?)\';', target_script_string).group(1)
            self.user.csrf = csrf_str
        except AttributeError:
            # AAA, ZZZ not found in the original string
            csrf_str = 'ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'  # apply your error handling
        except:
            print("可能cookie过期了! Error during get stock details, cookie may exired!!!")
            return -1
