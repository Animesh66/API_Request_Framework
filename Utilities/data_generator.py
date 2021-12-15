import logging as logger
import random
import string


def generate_email_password(domain=None, email_prefix=None):
    logger.info("Generating random email and password")
    if not domain:
        domain = 'testemail.com'
    if not email_prefix:
        email_prefix = 'testuser'

    email_length = 10
    email_string = "".join(random.choice(string.ascii_lowercase, k=email_length))
    email = email_prefix + '_' + email_string + '@' + domain

    password_length = 15
    password = "".join(random.choice(string.ascii_letters, k=password_length))
    generator = {'email': email, 'password': password}
    return generator

