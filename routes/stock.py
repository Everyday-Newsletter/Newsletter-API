import requests
from .helpStocks import get_all_stock_data
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
    c = 0
    for ticker in tickers:
        images = get_all_stock_data(ticker)
        if(not images):
            continue

        for image in images:
            c+=1
            html += f'<img src="data:image/png;base64,{image}" class="blog-image">'
        
    # return str(c)
    return render_template_string(html)

