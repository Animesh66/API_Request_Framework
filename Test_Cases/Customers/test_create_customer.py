from Helpers.Customer_Helper import CustomerHelper
import pytest


@pytest.mark.tcid_create_customer_1
def test_create_customer(woo_api_test):
    customer_helper = CustomerHelper()
    customer_helper.create_customer()
    customer_helper.verify_created_email()
