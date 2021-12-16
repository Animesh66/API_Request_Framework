import json
from Utilities.data_generator import generate_email_password
from Utilities.requests_utility import RequestsUtility


class CustomerHelper:

    def __init__(self):
        self.requests_util = RequestsUtility()
        self.email = None
        self.password = None

    def create_customer(self, **kwargs):
        generator = generate_email_password()
        self.email = generator['email']
        self.password = generator['password']
        payload = dict()
        payload['email'] = self.email
        payload['password'] = self.password
        payload.update(kwargs)
        response = self.requests_util.post('customers', payload=json.dumps(payload), expected_status_code=201)
        self.response_json = response.json()
        return self.response_json

    def verify_created_email(self):
        assert self.email == self.response_json['email'], f"The given email {self.email} " \
                                                        f"is matching the response email {self.response_json['email']}"
