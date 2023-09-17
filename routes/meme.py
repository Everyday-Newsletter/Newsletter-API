import random
import requests
from flask import request, Blueprint

meme_api = Blueprint("meme_api", __name__)

def get_json(url = None):
    if not url:
        return
    response = requests.get(url)
    if (response.status_code >= 300 or response.status_code < 200):
        return
    return response.json()

def call_url(my_url):
    caller_url = my_url
    return get_json(caller_url)

def get_one_meme():
    url_lst = [call_url(f"https://meme-api.com/gimme/wholesomememes"), 
               call_url(f"https://meme-api.com/gimme/memes"), 
               call_url(f"https://meme-api.com/gimme/meme")
               ]
    meme_lst = list(filter(lambda x: x and not x['nsfw'], url_lst))
    img = random.choice(meme_lst)['url']
    return img

@meme_api.route("/meme", methods=["GET"])
def meme():
    return get_one_meme()






    







