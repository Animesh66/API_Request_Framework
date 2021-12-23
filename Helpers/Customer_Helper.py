import json
import logging
from Utilities.data_generator import generate_email_password
from Utilities.logging_utility import Logger
from Utilities.requests_utility import RequestsUtility

log = Logger(__name__, logging.INFO)


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
        log.logger.info(f"Generated email is {self.email} and generated password is {self.password}")
        payload = dict()
        payload['email'] = self.email
        payload['password'] = self.password
        payload.update(kwargs)
        post_response = self.requests_util.post('customers', payload=json.dumps(payload), expected_status_code=201)
        self.post_response_json = post_response.json()
        log.logger.info(f"post response is {self.post_response_json}")
        return self.post_response_json

    def verify_created_email(self):
        assert self.email == self.post_response_json['email'], f"The given email {self.email} " \
                                                               f"is not matching with the response email " \
                                                               f"{self.post_response_json['email']} "
        log.logger.info("Email verification completed.")

    def get_customers(self, **kwargs):
        get_response = self.requests_util.get('customers', expected_status_code=200)
        self.get_response_json = get_response.json()
        log.logger.info(f"Get response received {self.get_response_json}")
        return self.get_response_json

    def create_existing_customer(self, existing_email):
        payload = dict()
        payload['email'] = existing_email
        payload['password'] = 'test1234'
        post_response = self.requests_util.post('customers', payload=json.dumps(payload), expected_status_code=400)
        log.logger.info(f"Post response receive is {post_response.json()}")
        return post_response
