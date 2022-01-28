from flask import Flask, render_template
from newsapi import NewsApiClient
from decouple import config
import datetime
from datetime import timedelta


app = Flask(__name__)
KEY = config('API_KEY')
newsapi = NewsApiClient(api_key=KEY)
today = datetime.datetime.now()
three_days_ago = (today - timedelta(days=3)).date()


@app.route('/')
@app.route('/index')
def index():
    news = newsapi.get_everything(sources="bbc-news,cnn,the-verge",
                                  from_param=three_days_ago,
                                  language='en')
    # Get articles list from the news dict
    articles = news['articles']
    return render_template('index.html', articles=articles)


@app.route('/get_news/<s>')
def get_news(s):
    news = newsapi.get_everything(sources=s,
                                  from_param=three_days_ago,
                                  language='en')
    articles = news['articles']
    return render_template('filter.html', articles=articles)


if __name__ == "__main__":
    app.run()
