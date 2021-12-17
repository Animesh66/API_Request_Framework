import pytest
import requests
from Configuration.hosts_config import consumer_key, consumer_secret


@pytest.mark.product_sanity
@pytest.mark.tcid_get_product_1
def test_get_all_products():
    # TODO convert this to helper classes
    response = requests.get("https://www.cheapgiftidea.com/wp-json/wc/v3/products",
                            auth=(consumer_key, consumer_secret))
    print("Response code is " + str(response.status_code))
    response_code = response.status_code
    assert response_code == 200, "Response code is NOT 200"
    print(response.url)
    print(response.headers['Content-Type'])
