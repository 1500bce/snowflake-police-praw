import util
import reddit_conn
import db
from datetime import datetime
import html
import time
from models.history import History
import sys

result = db.get_data()
comment_ids = []
for data in result:
    comment_ids.append(data[5])

reddit = reddit_conn.launch_reddit_conn()

response = util.get_response()

now = datetime.now()
# now.hour
time_of_day = util.get_time_of_day(now.hour)
# print(time_of_day)
# ---- SEARCH SUBREDDIT SUBMISSIONS ----

submissions = reddit.subreddit("Philippines").search(query=f"{time_of_day} random discussion", sort='new', time_filter='day')

# comment_stream = reddit.subreddit("Philippines").stream.comments(skip_existing=True)

for thread in submissions:
    submission = thread
# submission = reddit.submission(id='b0fwbj')



ctr = 0
submission.comments.replace_more(limit=None)
print(f"Found {submission.num_comments} comment(s).")
for comment in submission.comments.list():
    print(f"{comment.author}: {comment.body}\n")
    ctr += 1
    snowflake_words = util.get_snowflake_words()
    for word in snowflake_words:
        if word in comment.body.upper() and comment.id not in comment_ids:
            # print(f"{comment.body}")
            comment.reply(response)
            history = History(comment.submission.id,
                              comment.submission.title,
                              html.escape(comment.submission.selftext),
                              comment.submission.created_utc,
                              comment.id,
                              comment.author,
                              html.escape(comment.body))
            db.insert_data(history)
            print(f"{comment.author}'s comment was affected.")
            time.sleep(6)
            continue


# input("End.")
# time.sleep(6)
# sys.exit()

