# filename: reddit_conn.py

import praw

def launch_reddit_conn():
    return praw.Reddit(client_id='NCUFJZ45IvjIuw',
                client_secret='rYeRqKlTxlB0MKLqLkErroCC3jo',
                password='Cmykm1234',
                user_agent='snowflake_detector',
                username='-SNOWFLAKE_DETECTOR-')