from datetime import datetime, date, timedelta
from twitterscraper import query_tweets


def get_last_month_tweets(query, limit=1000, lang="es"):
    start_date = date.today() - timedelta(30)
    tweets = query_tweets(query, limit, poolsize=5, lang=lang, begindate=start_date)
    print(f"Got {len(tweets)} tweets.")
    return tweets

def get_last_half_year_tweets(query, limit=1000, lang="es"):
    start_date = date.today() - timedelta(30*6)
    tweets = query_tweets(query, limit, poolsize=5, lang=lang, begindate=start_date)
    print(f"Got {len(tweets)} tweets.")
    return tweets
