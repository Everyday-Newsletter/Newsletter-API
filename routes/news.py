import requests, os, json, random
from flask import Blueprint, request

news_api = Blueprint("news_api", __name__)

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_CATEGORIES = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology",
]


def get_news(category, country):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize=8&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    json_format = response.json()

    if (
        json_format["status"].lower() != "ok".lower()
        or response.status_code < 200
        or response.status_code >= 300
        or json_format["totalResults"] <= 0
    ):
        return []

    return [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "image-url": article["urlToImage"],
        }
        for article in json_format["articles"]
    ]


@news_api.route("/news")
def news():
    category = request.args.get("category", "").lower()
    if not category:
        category = random.choice(NEWS_CATEGORIES)

    elif category not in NEWS_CATEGORIES:
        return f"Invalid category! Pick from: {', '.join(NEWS_CATEGORIES)}", 403

    country = request.args.get("country", "").lower()

    if not country:
        country = "US"

    return get_news(category, country)
