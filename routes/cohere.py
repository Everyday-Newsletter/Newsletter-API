import requests
from flask import request, Blueprint
import json

cohere_api = Blueprint("cohere_api", __name__)



def get_cohere(inp):
    url = "https://api.cohere.ai/v1/chat"

    payload = {
        "message": "Based on my response give me advice for the day.",
        "temperature": 0.5,
        "stream": False,
        "chat_history": [
            {
                "user_name": "User",
                "message": inp
            },
            {
                "user_name": "Chatbot",
                "message": "How are you doing today?"
            }
        ],
        "prompt_truncation": "OFF"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer J0pxW49Jt8qDsdTY5KEjSix7hzzQlQXoKsfKPVK5"
    }

    response = requests.post(url, json=payload, headers=headers)
    json_format = json.loads(response.text)
    return json_format["text"]


@cohere_api.route("/mental_health", methods=["GET"])
def mental_health():
    message = request.args.get("message", "").strip()
    if not message:
        return "Please provide 'message' parameter", 403


    return get_cohere(message)
