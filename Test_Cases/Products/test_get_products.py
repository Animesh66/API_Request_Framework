import requests
import os


consumer_key = os.getenv("WOO_CONSUMER_KEY")
consumer_secret = os.getenv("WOO_CONSUMER_SECRET")


def test_get_products():
    response = requests.get("https://www.cheapgiftidea.com/wp-json/wc/v3/products",
                            auth=(consumer_key, consumer_secret))
    print("Response code is " + str(response.status_code))
    response_code = response.status_code
    assert response_code == 200, "Response code is NOT 200"
    print(response.url)
    print(response.headers['Content-Type'])
