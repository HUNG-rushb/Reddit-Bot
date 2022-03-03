import praw

reddit = praw.Reddit(client_id='lTxGUPTXNXbF1RVUTeDTcw',
                     client_secret='x-DXoRwI50QPwnvxpZ1lZkDvr52fxQ',
                     user_agent='a reddit instance',
                     username='DuyHungVN',
                     password='h6h5h4h3h2h1',
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