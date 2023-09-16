import requests
import random
from flask import Blueprint, request

bored_api = Blueprint("bored_api", __name__)

ACTIVITY_TYPES = [
    "charity",
    "social",
    "diy",
    "education",
    "relaxation",
    "recreational",
    "music",
    "cooking",
    "busywork",
]


def get_activity(task_type):
    response = requests.get(f"https://www.boredapi.com/api/activity?type={task_type}")
    return response.json().get("activity")


@bored_api.route("/activity", methods=["GET"])
def activity():
    activity_type = request.args.get("type", "").lower()
    if not activity_type:
        activity_type = random.choice(ACTIVITY_TYPES)

    elif activity_type not in ACTIVITY_TYPES:
        return f"Invalid type! Pick from: {', '.join(ACTIVITY_TYPES)}", 403

    return get_activity(activity_type)
