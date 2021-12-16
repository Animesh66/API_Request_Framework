import json

from Utilities.data_generator import generate_email_password
from Utilities.requests_utility import RequestsUtility


class CustomerHelper:

    def __init__(self):
        self.requests_util = RequestsUtility()

    def create_customer(self, **kwargs):
        generator = generate_email_password()
        email = generator['email']
        password = generator['password']
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
        self.requests_util.post('customers', payload=json.dumps(payload), expected_status_code=201)
