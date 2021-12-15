from Utilities.data_generator import generate_email_password


class CustomerHelper:

    def __init__(self):
        pass

    def create_customer(self, **kwargs):
        generator = generate_email_password()
        email = generator['email']
        password = generator['password']
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)
