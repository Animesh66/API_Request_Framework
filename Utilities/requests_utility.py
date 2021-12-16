import os
import requests
from Configuration.hosts_config import API_HOSTS, consumer_key, consumer_secret
from requests_oauthlib import OAuth1


class RequestsUtility:

    def __init__(self):
        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(consumer_key, consumer_secret)

    def post(self, endpoint, payload=None, header=None, expected_status_code=None):
        if not header:
            header = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        post_response = requests.post(url=url, data=payload, headers=header, auth=self.auth)
        actual_status_code = post_response.status_code
        if not expected_status_code:
            actual_status_code = None
        assert expected_status_code == actual_status_code, \
            f"expected status code is {expected_status_code} but actual status code is {actual_status_code}"
        return post_response

    def get(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
