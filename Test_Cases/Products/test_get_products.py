import requests

consumer_key = 'ck_39fa25f6979b191dc83dcbcd64162d0fdb81dd14'
consumer_secret = 'cs_0ea26b08f4793747920bfa2fa36130502dc1d0b5'


def test_get_products():
    response = requests.get("https://www.cheapgiftidea.com/wp-json/wc/v3/products",
                            auth=(consumer_key, consumer_secret))
    print("Response code is " + str(response.status_code))
    response_code = response.status_code
    assert response_code == 200, "Response code is NOT 200"
    print(response.url)
    print(response.headers['Content-Type'])
