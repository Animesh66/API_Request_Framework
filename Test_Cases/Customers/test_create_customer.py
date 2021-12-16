from Helpers.Customer_Helper import CustomerHelper
import pdb


def test_create_customer():
    customer_helper = CustomerHelper()
    customer_helper.create_customer()
    pdb.set_trace()
    customer_helper.verify_created_email()
