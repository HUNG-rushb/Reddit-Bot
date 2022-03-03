import praw

reddit = praw.Reddit(client_id='FKpsepQaSNHd0PQBphUc9Q',
                     client_secret='uw7y1aXVF2fgorIdwOxokdnxUgsUSQ',
                     user_agent='trinh duy hung',
                     username='hung-bot',
                     password='tdhvn1352001',
                     check_for_async=False)


import requests
import bs4
import random
import time

trigger_phrase = "fact"

messages = reddit.inbox.stream()

for message in messages:
  try:
    if message in reddit.inbox.mentions() and message in reddit.inbox.unread():
      if trigger_phrase in message.body:
        res = requests.get("https://www.kickassfacts.com/fact-of-the-day/")
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        soupy = soup.select("div > ol > li")
        ran_int = random.randint(1,30)
        fact = soupy[ran_int].getText()
        fact = fact[:-8]

        message.reply(fact)
        message.mark_read()
	# print(fact)

  except praw.exception.APIException:
    print("Probably a rate limit :(")

  time.sleep(15)

