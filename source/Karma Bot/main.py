import praw

reddit = praw.Reddit(client_id='',
                     client_secret='x-',
                     user_agent='a reddit ',
                     username='',
                     password='',
                     check_for_async=False)

import random
import time

def karma():
  try:
    messages = [".", ":", "?"]

    for submission in reddit.subreddit("FreeKarma4U+FreeKarma4You").stream.submissions():
      submission.upvote()

      rand = random.randint(0, (len(messages)-1))
      print(submission.title)
      submission.reply(messages[rand])

      time.sleep(30)
  except:
    time.sleep(300)
    karma()

karma()
