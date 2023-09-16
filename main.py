from flask import Flask

# Routes
from routes.joke import joke_api
from routes.bored import bored_api

app = Flask(__name__)
app.register_blueprint(joke_api)  # /joke
app.register_blueprint(bored_api)  # /activity

# Port 8080 on all interfaces
app.run("0.0.0.0", port=8080)
