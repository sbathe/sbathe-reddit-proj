#!/usr/bin/python
""" A very basic bot. Gets 100 new entries every 5 minutes and stores required
    parameters"""
import praw, sqlite3, time
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS new
              (title text, subreddit text, subredditid text, created float, 
               score int, ups int, downs int, user text, username text, 
               text text, url text, fullname text, trackscore BOOLEAN)''')
cur.execute(''' CREATE UNIQUE INDEX IF NOT EXISTS fullname on new(fullname)''') 
cur.execute(''' CREATE INDEX IF NOT EXISTS created on new(fullname)''') 

rdt = praw.Reddit('topiwalla-newbot')
already_done = []
cur.execute("select fullname from new")
ids = cur.fetchall()
already_done = [ e[0] for e in ids if e not in already_done ]

### Replaced by the list comprehension above
#for e in ids:
#    if e[0] not in already_done:
#        already_done.append(e[0])

new_reddits = []
new_ids = []

while True:
    for submission in rdt.get_new(limit=100):
        if submission.fullname not in already_done:
            if submission.fullname not in new_ids:
                # dump everything into a list or tuples
                print "Adding %s to new ids" % submission.fullname
                new_ids.append(submission.fullname)
                new_reddits.append((submission.title,
                   submission.subreddit.title,
                   submission.subreddit_id, submission.created_utc, 
                   submission.score, submission.ups, submission.downs, 
                   submission.author.name, submission.author.fullname, 
                   submission.selftext, submission.url, submission.fullname, 1))
    try:
      cur.executemany("INSERT INTO new values (?,?,?,?,?,?,?,?,?,?,?,?,?)", 
          new_reddits)
    except sqlite3.Error as e:
      print "Error: %s: %s" % (e.args[0], submission.fullname)
    cur.connection.commit()
    already_done.extend(new_ids)
    new_ids = []
    time.sleep(300)
