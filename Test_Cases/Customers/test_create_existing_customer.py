from Helpers.Customer_Helper import CustomerHelper
import pytest


@pytest.mark.customer_sanity
@pytest.mark.tcid_create_customer_2
def test_create_exiting_customer(woo_api_test):
    customer_helper = CustomerHelper()
    create_response = customer_helper.create_customer()
    created_email = create_response['email']
    customer_helper.create_existing_customer(existing_email=created_email)


