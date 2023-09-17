import requests
from .helpStocks import get_all_stock_data
from flask import request, Blueprint, render_template_string

stock_api = Blueprint("stock_api", __name__)

tickers = [
    "AAPL",
    "MSFT",
    "2222.SR",
    "GOOG",
    "AMZN",
    "NVDA",
    "META",
    "TSLA",
    "V",
]


@stock_api.route("/stocks", methods=["GET"])
def stocks():
    plots = []
    for ticker in tickers:
        images = get_all_stock_data(ticker)
        if not images:
            continue
        plots.append(images)

    return plots
