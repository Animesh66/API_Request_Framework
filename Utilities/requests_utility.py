import os
import requests
from Configuration.hosts_config import API_HOSTS


class RequestsUtility:

    def __init__(self):
        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]

    def post(self, endpoint, payload=None, header=None):
        if not header:
            header = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        post_response = requests.post(url=url, data=payload, headers=header)
        # print(post_response.status_code)

    def get(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
