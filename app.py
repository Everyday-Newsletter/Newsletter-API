from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

from flask import Flask
from flask_cors import CORS

# Routes
from routes.cohere import cohere_api
from routes.joke import joke_api
from routes.bored import bored_api
from routes.news import news_api
from routes.stock import stock_api
from routes.meme import meme_api
from routes.memes import memes_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(cohere_api)  # /mental_health
app.register_blueprint(joke_api)  # /joke
app.register_blueprint(bored_api)  # /activity
app.register_blueprint(news_api)  # /news
app.register_blueprint(stock_api)  # /stocks
app.register_blueprint(meme_api)  # /meme
app.register_blueprint(memes_api)  # /memes

# Port 8080 on all interfaces
if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)
