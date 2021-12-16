from Helpers.Customer_Helper import CustomerHelper


def test_create_customer(woo_api_test):
    customer_helper = CustomerHelper()
    customer_helper.create_customer()
    customer_helper.verify_created_email()
