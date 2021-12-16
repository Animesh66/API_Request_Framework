from Helpers.Customer_Helper import CustomerHelper
import pytest


@pytest.mark.tcid_get_customer_2
def test_get_all_customers(woo_api_test):
    customer_helper = CustomerHelper()
    customer_helper.get_customers()