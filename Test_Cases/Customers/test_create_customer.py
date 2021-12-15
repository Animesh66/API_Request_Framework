import requests
from Utilities.data_generator import generate_email_password


def test_create_customer():
    generator = generate_email_password()
    email = generator['email']
    password = generator['password']
    payload = {'email': email, 'password': password}