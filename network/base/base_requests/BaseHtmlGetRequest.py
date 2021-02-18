from bs4 import BeautifulSoup
from network.base.base_requests.BaseRequest import BaseRequest


class BaseHtmlGetRequest(BaseRequest):

    def __init__(self, cookie, additional_headers_dict, url):
        super().__init__(cookie, additional_headers_dict, url)
        self.soup = None

    def process_response(self):
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.process_html_soup_result()
        return self.soup

    def process_html_soup_result(self):
        pass