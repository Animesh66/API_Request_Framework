import logging
from Helpers.Customer_Helper import CustomerHelper
import pytest

from Utilities.logging_utility import Logger

log = Logger(__name__, logging.INFO)


@pytest.mark.customer_sanity
@pytest.mark.tcid_get_customer_1
def test_get_all_customers(woo_api_test):
    log.logger.info("****** TEST GET CUSTOMER EXECUTION STARTED ******")
    customer_helper = CustomerHelper()
    customer_helper.get_customers()
    log.logger.info("****** TEST GET CUSTOMER EXECUTION FINISHED ******")