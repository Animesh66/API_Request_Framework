import logging
import os
from urllib.parse import urljoin
import requests
from Configuration.hosts_config import API_HOSTS, consumer_key, consumer_secret
from requests_oauthlib import OAuth1
from Utilities.logging_utility import Logger

log = Logger(__name__, logging.INFO)


class RequestsUtility:

    def __init__(self):
        self.env = os.getenv("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(consumer_key, consumer_secret)

    def post(self, endpoint, payload=None, header=None, expected_status_code=None):
        if not header:
            header = {"Content-Type": "application/json"}
        url = urljoin(self.base_url, endpoint)
        # url = self.base_url + endpoint
        post_response = requests.post(url=url, data=payload, headers=header, auth=self.auth)
        log.logger.info("post response executed.")
        actual_status_code = post_response.status_code
        if not expected_status_code:
            actual_status_code = None
        assert expected_status_code == actual_status_code, \
            f"expected status code is {expected_status_code} but actual status code is {actual_status_code}"
        # log.logger.info(f"API response is {post_response.json()}")
        return post_response

    def get(self, endpoint, header=None, expected_status_code=None):
        if not header:
            header = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        get_response = requests.get(url=url, headers=header, auth=self.auth)
        actual_status_code = get_response.status_code
        if not expected_status_code:
            actual_status_code = None
        assert expected_status_code == actual_status_code, \
            f"expected status code is {expected_status_code} but actual status code is {actual_status_code}"
        log.logger.info(f"API response is {get_response.json()}")
        return get_response

    def update(self):
        pass

    def delete(self):
        pass
