import tweepy

print('this is my twitter bot')

CONSUMER_KEY = '6znNlDiQhyKJHNps7LOErfH0m'
CONSUMER_SECRET = 'CDVisqN8bC6XDDnBpRoiVGt7pJ4qPxjYm2TZ6Aw8lesc6avC76'
ACCESS_KEY = '188737558-vUJ8innuVdi4VN4WzSZGmVsPzxKTYaRb9JFFyKe8'
ACESS_SECRET = 'GiDpwzKwaVs6xVN4ALyqmh2QJm8vNyZo5QmEep3JeSbx0'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)
api = tweepy.API(auth)

search_word = "#駆け出しエンジニア"
search_results_list = api.search(q=search_word, count=20)

for tweet in search_results_list:
    try:
        api.create_favorite(tweet.id)
        print(tweet.text)
    except:
        print("I failed to create favorite.")
