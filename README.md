sbathe-reddit-proj
==================

reddit-project

Phase 1
1. Write a bot to get and store data from reddit: (either pickle it or put it in simple csv file)
   Title, subreddit, date and time of posting it, upvotes, the username of the poster, url, fullname
     a. from all new posts every 5 minutes
     b. from top 100 posts every 30 minutes (get same data as above)
2. For all posts, store comments also: text, commentor id, date

Phase 2:
1. Check if any of the id featuring in the top reddits is one of the ids we have in store
2. For all ids in store check if their score is increasing (we will need to worry about rate later)
  a. if it is increasing, get snapshots and store them ( snapid (generate),score, datetime)
  b. if not remove it from our list 
3. Do the above at 30 minutes interval

Phase 3:
1. For all urls we have, start crawling 
  a. if it is a image, just dump it with filename as the name of post
  b. if it is link to a text doc, index keywords (post fullname, list of keywords)
  c. do nothing for a video url

