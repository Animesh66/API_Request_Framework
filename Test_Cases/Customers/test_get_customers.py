from Helpers.Customer_Helper import CustomerHelper
import pytest


@pytest.mark.customer_sanity
@pytest.mark.tcid_get_customer_1
def test_get_all_customers(woo_api_test):
    customer_helper = CustomerHelper()
    customer_helper.get_customers()