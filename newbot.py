#!/usr/bin/python
import praw, sqlite3, time
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS new
              (title text, subreddit text, subredditid text, created float, score int, ups int, downs int, user text, username text, text text, url text, fullname text)''')

r = praw.Reddit('topiwalla-newbot')
already_done = []
c.execute("select fullname from new")
ids = c.fetchall()
for id in ids:
  if id[0] not in already_done:
    already_done.append(id[0])
new_reddits = []
new_ids = []
while True:
  for submission in r.get_new(limit=100):
    if submission.fullname not in already_done:
      if submission.fullname not in new_reddits:
        # dump everything into a list or tuples
        print "Adding %s to new ids" % submission.fullname
        new_reddits.append((submission.title, submission.subreddit.title, submission.subreddit_id, submission.created_utc, submission.score, submission.ups, submission.downs, submission.author.name, submission.author.fullname, submission.selftext, submission.url, submission.fullname))
        new_ids.append(submission.fullname)

  c.executemany("INSERT INTO new values (?,?,?,?,?,?,?,?,?,?,?,?)", new_reddits)
  c.connection.commit()
  already_done.extend(new_ids)
  new_ids = []
  time.sleep(300)
