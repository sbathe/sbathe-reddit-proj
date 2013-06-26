#!/usr/bin/python
import praw, sqlite3, time
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("select fullname from new where trackscore=1")
track_ids = [ id[0].split('_')[1] for id in cur.fetchall() ]
while track_ids:
  for id in track_ids:
    submission = rdt.get_submission(submission_id=id)
    slist = [ id, submission.score ]
