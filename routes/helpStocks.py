import yfinance as yf
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt

import datetime as dt
import sys
import os

# Encode Images
import base64
import io

dirPath = 'static/graphs/'

def mysavefig(ticker, number, dirPath):
    filePath = dirPath + ticker + str(number) + ".jpg"
    if os.path.isfile(filePath):
        os.remove(filePath)   # Opt.: os.system("rm "+strFile)
    plt.savefig(filePath)


def get_all_stock_data(ticker):
    if not _is_valid_symbol(ticker):
        return None

    graphs = [get_year(ticker), get_month(ticker), get_intraday(ticker)]
    return graphs


def get_year(ticker):
    today = dt.datetime.today()

    if today.month > 11:
        startMonth = today.month - 11
        startYear = today.year
    else:
        startMonth = today.month + 1
        startYear = today.year - 1
    data = _get_data(dt.datetime(startYear, startMonth, 1), today, ticker)

    mysavefig(ticker, 0, dirPath)



def get_month(ticker):
    today = dt.datetime.today()

    if today.month == 1:
        startMonth = today.month + 11
        startYear = today.year - 1
    else:
        startMonth = today.month - 1
        startYear = today.year
    data = _get_data(dt.datetime(startYear, startMonth, 1), today, ticker)
    mysavefig(ticker, 1, dirPath)



def get_intraday(ticker):
    data = yf.download(ticker, period="1d", interval="1m")
    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"])
    company_name = yf.Ticker(ticker).info["longName"]
    plt.title(company_name + ": Historical Stock Value")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    mysavefig(ticker, 2, dirPath)



def _get_data(start, end, ticker):
    data = yf.download(ticker, start, end)

    # Visualizing the fetched data
    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"])
    company_name = yf.Ticker(ticker).info["longName"]
    plt.title(company_name + ": Historical Stock Value")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")

    return data


def _is_valid_symbol(ticker):
    info = yf.Ticker(ticker).history(period="7d", interval="1d")

    return len(info) > 0
