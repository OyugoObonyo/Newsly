import flask
from flask import Flask
from newsapi import NewsApiClient


app = Flask(__name__) 
newsapi = NewsApiClient(api_key='e1dda8521e944c7d8b572531800c210e')
sources = newsapi.get_sources()['sources']


@app.route('/')
@app.route('/index')
def index():
    pass


@app.route('/get_news/<keyword>')
def get_news():
    pass
