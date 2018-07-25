import tweepy
from tweepy import OAuthHandler
import requests
import os

# consumer key
API_KEY = "4jHYLlPZiVG1GIJgtlMLo0zhb"
API_SECRET_KEY = "ibDeUajo0UuQ0FjOW3zZNaFLcrul12ronf4QJlpvaBuVu36n1t"
ACCESS_TOKEN = "1018003367883239424-Ik46XiG2XPadhLoHj0yVHXf21UgKJy"
ACCESS_TOKEN_SECRET = "LtKhHBldif9ejCOd96w5MvjEhjQEb09W7PmB0U9ImHnUE"

auth = OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_shiba(obj):
    return obj.json()[0]

def tweet_image(url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename=filename,
                              status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

raw_shib = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
shib = get_shiba(raw_shib)
msg = "Hourly shiba: test run"
tweet_image(shib, msg)
