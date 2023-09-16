from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

from flask import Flask

# Routes
from routes.joke import joke_api
from routes.bored import bored_api
from routes.news import news_api
from routes.stock import stock_api

app = Flask(__name__)
app.register_blueprint(joke_api)  # /joke
app.register_blueprint(bored_api)  # /activity
app.register_blueprint(news_api)  # /news
app.register_blueprint(stock_api) #/stocks

# Port 8080 on all interfaces
app.run("0.0.0.0", port=8080)
