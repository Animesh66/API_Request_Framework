import requests
from Configuration.hosts_config import consumer_key, consumer_secret




def test_get_products():
    response = requests.get("https://www.cheapgiftidea.com/wp-json/wc/v3/products",
                            auth=(consumer_key, consumer_secret))
    print("Response code is " + str(response.status_code))
    response_code = response.status_code
    assert response_code == 200, "Response code is NOT 200"
    print(response.url)
    print(response.headers['Content-Type'])
