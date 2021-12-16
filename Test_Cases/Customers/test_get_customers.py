from Helpers.Customer_Helper import CustomerHelper
import pytest


@pytest.mark.tcid_get_customer_2
def test_create_customer(woo_api_test):
    customer_helper = CustomerHelper()
    customer_helper.get_customers()