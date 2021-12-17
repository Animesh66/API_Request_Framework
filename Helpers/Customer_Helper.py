import json
from Utilities.data_generator import generate_email_password
from Utilities.requests_utility import RequestsUtility
import logging as logger

class CustomerHelper:

    def __init__(self):
        self.get_response_json = None
        self.post_response_json = None
        self.requests_util = RequestsUtility()
        self.email = None
        self.password = None

    def create_customer(self, **kwargs):
        generator = generate_email_password(domain='mytest.com.au', email_prefix='runtest')
        self.email = generator['email']
        self.password = generator['password']
        payload = dict()
        payload['email'] = self.email
        payload['password'] = self.password
        payload.update(kwargs)
        post_response = self.requests_util.post('customers', payload=json.dumps(payload), expected_status_code=201)
        self.post_response_json = post_response.json()
        return self.post_response_json

    def verify_created_email(self):
        assert self.email == self.post_response_json['email'], f"The given email {self.email} " \
                    f"is not matching with the response email {self.post_response_json['email']}"

    def get_customers(self, **kwargs):
        get_response = self.requests_util.get('customers', expected_status_code=200)
        self.get_response_json = get_response.json()
        return self.get_response_json

    def create_existing_customer(self, existing_email):
        payload = dict()
        payload['email'] = existing_email
        payload['password'] = 'test1234'
        post_response = self.requests_util.post('customers', payload=json.dumps(payload), expected_status_code=400)
        logger.info(f"Post response receive is {post_response.json()}")
        return post_response
