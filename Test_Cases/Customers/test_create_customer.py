import logging
from Helpers.Customer_Helper import CustomerHelper
import pytest
from Utilities.logging_utility import Logger

log = Logger(__name__, logging.INFO)


@pytest.mark.customer_sanity
@pytest.mark.tcid_create_customer_1
def test_create_customer(woo_api_test):
    log.logger.info("****** TEST CREATE CUSTOMER EXECUTION STARTED ******")
    customer_helper = CustomerHelper()
    customer_helper.create_customer()
    customer_helper.verify_created_email()
    log.logger.info("****** TEST CREATE CUSTOMER EXECUTION FINISHED ******")