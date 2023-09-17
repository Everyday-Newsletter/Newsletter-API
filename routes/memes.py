import random
import requests
from flask import request, Blueprint

memes_api = Blueprint("memes_api", __name__)


def get_json(url=None):
    if not url:
        return
    response = requests.get(url)
    if response.status_code >= 300 or response.status_code < 200:
        return
    return response.json()


def call_url(my_url):
    caller_url = my_url
    return get_json(caller_url)


def get_several_memes():
    url_lst = [
        call_url(f"https://meme-api.com/gimme/wholesomememes/50"),
        call_url(f"https://meme-api.com/gimme/memes/50"),
        call_url(f"https://meme-api.com/gimme/meme/50"),
    ]
    img_lst = []
    meme_dict = random.choice(url_lst)
    meme_lst = meme_dict["memes"]
    valid_lst = list(filter(lambda x: x and not x["nsfw"], meme_lst))
    img_lst = [a["url"] for a in valid_lst]
    return img_lst


@memes_api.route("/memes", methods=["GET"])
def memes():
    return get_several_memes()
