import requests
from flask import request, Blueprint

joke_api = Blueprint("joke_api", __name__)


def generate_joke(type="misc"):
    url = f"https://v2.jokeapi.dev/joke/{type}?blacklistFlags=nsfw,religious,political,racist,sexist&type=single"
    response = requests.get(url)
    json_format = response.json()

    if (
        response.status_code >= 200
        and response.status_code < 300
        and json_format["error"] == False
    ):
        return json_format["joke"]


@joke_api.route("/joke", methods=["GET"])
def joke():
    joke_type = request.args.get("type") or "misc"
    if joke_type not in ["programming", "pun", "misc"]:
        return "Invalid type! Pick from 'programming', 'pun', 'misc'", 403

    return generate_joke(joke_type)
