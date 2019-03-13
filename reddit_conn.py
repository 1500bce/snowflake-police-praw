# filename: reddit_conn.py

import praw

def launch_reddit_conn():
    return praw.Reddit(client_id='xx',
                client_secret='xxx',
                password='xxx',
                user_agent='snowflake_detector',
                username='-SNOWFLAKE_DETECTOR-')
