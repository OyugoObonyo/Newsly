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
    articles = newsapi.get_everything()
    return render_template('index.html', articles=articles)


@app.route('/get_news/<keyword>')
def get_news():
    pass
