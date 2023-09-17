import requests
from .helpStocks import get_all_stock_data, dirPath
from flask import request, Blueprint, render_template_string

stock_api = Blueprint("stock_api", __name__)

tickers = ["AAPL", 
           "MSFT", 
           "2222.SR",
           "GOOG",
           "AMZN",
           "NVDA",
           "META",
           "TSLA",
           "MC.PA",
           "V"]

@stock_api.route("/stocks", methods=["GET"])
def stocks():
    html=''
    for ticker in tickers:
        images = get_all_stock_data(ticker)
        if(not images):
            continue

        for i in range(3):
            filePath = dirPath + ticker + str(i) + ".jpg"
            html += f'<img src="{filePath}" class="blog-image">'
        
    return render_template_string(html)

