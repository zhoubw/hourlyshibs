import tweepy # pip
from tweepy import OAuthHandler
import requests # pip
import os
from apscheduler.schedulers.blocking import BlockingScheduler # pip
import random

# consumer key
API_KEY = "4jHYLlPZiVG1GIJgtlMLo0zhb"
API_SECRET_KEY = "ibDeUajo0UuQ0FjOW3zZNaFLcrul12ronf4QJlpvaBuVu36n1t"
ACCESS_TOKEN = "1018003367883239424-Ik46XiG2XPadhLoHj0yVHXf21UgKJy"
ACCESS_TOKEN_SECRET = "LtKhHBldif9ejCOd96w5MvjEhjQEb09W7PmB0U9ImHnUE"

auth = OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_shiba_from_raw(obj):
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

labels = ["shib", "woofer", "subwoofer", "doggo", "doge", "shibro", "shiboi"]
secure_random = random.SystemRandom()
def hourly_shib():
    raw_shib = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
    shib = get_shiba_from_raw(raw_shib)
    msg = secure_random.choice(labels)
    tweet_image(shib, msg)
    print(shib)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(temp, 'interval', hours=1)
    scheduler.start()

    print("started job")

    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
