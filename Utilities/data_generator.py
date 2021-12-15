import logging as logger
import random
import string


def generate_email_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")
    if not domain:
        domain = 'testemail.com'
    if not email_prefix:
        email_prefix = 'testuser'

    email_length = 10
    email_string = ''.join(random.choices(string.ascii_lowercase, k=email_length))
    email = email_prefix + '_' + email_string + '@' + domain

    password_length = 15
    password = ''.join(random.choices(string.ascii_letters, k=password_length))
    generator = {'email': email, 'password': password}
    logger.debug(f"Email id generated is {generator['email']} and password generated is {generator['password']}")
    return generator


# var_ep = generate_email_password(domain="santa.com.au", email_prefix="animesh")
# print(var_ep)
