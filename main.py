from flask import Flask

app = Flask(__name__)

@app.route("/joke", methods=["GET"])
def get_joke():
    url = ('https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist&type=single')
    response = requests.get(url)
    json_format = response.json()

    if(response.status_code >= 200 and response.status_code < 300 and json_format["error"] == False):
        return json_format["joke"]
    
    return None

# Port 8080 on all interfaces
app.listen('0.0.0.0', port=8080)
