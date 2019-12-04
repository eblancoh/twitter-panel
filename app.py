from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from textblob import TextBlob
from textblob.exceptions import NotTranslated
from scraper import get_last_half_year_tweets, get_last_month_tweets
from preprocessing import process_text
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("landing.html")


@app.route("/dash", methods=['POST'])
def dash():
    query = request.form.get("query")
    print("got query of", query)
    tweets = get_last_month_tweets(query)
    columns = ['fullname', 'is_retweet', 'likes',
               'replies', 'retweet_id', 'retweeter_userid', 'retweeter_username', 'retweets',
               'text', 'timestamp', 'tweet_id', 'user_id', 'username', 'tweet_url']
    tweets_df = pd.DataFrame(columns=columns)

    for tweet in tweets:
        tweet_dict = {}
        for att in columns:
            tweet_dict[att] = getattr(tweet, att)
        tweets_df = tweets_df.append(tweet_dict, ignore_index=True)

    try:
        tweets_text = list(tweets_df['text'])
        total_tweets = len(tweets_df)
        total_retweets = tweets_df['retweets'].sum()
        total_likes = tweets_df['likes'].sum()
        responses = process_text(tweets_text, query)
        styles = ["primary", "success", "info", "warning", "danger", "secondary"]

        # Sentiment Analysis. Sacamos la polaridad del sentimiento
        tweets_df['sentiment'] = tweets_df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
        pos_sent = np.where(tweets_df['sentiment']>=-0.05)[0].__len__()
        neg_sent = np.where(tweets_df['sentiment']<-0.05)[0].__len__()

        # sort tweets by likes then retweets and get the top 6 tweets
        tweets_df = tweets_df.sort_values(['retweets', 'likes'], ascending=False)
        tweets_df = tweets_df.drop_duplicates('text')
        tweets_df['text'] = tweets_df['text'].apply(lambda x: x.strip())
        top_tweets = tweets_df.iloc[:3, :].to_dict("records")


        return render_template("dashboard.html", query=query, total_tweets=total_tweets,
        total_retweets=total_retweets, total_likes=total_likes, hashtags=zip(responses['hashtags'], styles),
        cloud_sign=responses['cloud_sign'], negative_counts=neg_sent, positive_counts=pos_sent, top_tweets=top_tweets)

    except ValueError:
        # En el caso de que no haya encontrado nada, WordCloud va a dar un ValueError. 
        # Renderizamos el error.
        return render_template("error500.html")

def to_landing():
    return redirect(url_for('landing.html'))

if __name__ == "__main__":
    app.run()