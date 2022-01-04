import os

API_HOSTS = {
    "test": "https://www.cheapgiftidea.com/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}

consumer_key = os.getenv("WOO_CONSUMER_KEY")
consumer_secret = os.getenv("WOO_CONSUMER_SECRET")