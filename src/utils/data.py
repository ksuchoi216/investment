import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

from datetime import datetime as dt

import yaml


def load_tickers(path="./config.yaml"):
    with open(path, "r") as file:
        tickers = yaml.safe_load(file)
    return tickers


def get_start_end_dates(years=5, start=None, end=None):
    if start is None:
        start = dt.today().replace(year=dt.today().year - years)

    if end is None:
        end = dt.today()

    end = end.strftime("%Y-%m-%d")
    start = start.strftime("%Y-%m-%d")

    return start, end


def get_ticker(ticker, start, end):
    df = pdr.get_data_yahoo(ticker, start=start, end=end)
    company = yf.Ticker(ticker)
    return df, company


def get_data(tickers, years, start=None, end=None):
    data_dic = {}
    for key, ticker in tickers.items():
        data_dic[key] = yf.Ticker(ticker)

    return data_dic


# def get_data(tickers, years, start=None, end=None):

#     data_dic = {}
#     for key, ticker in tickers.items():
#         # _start, _end = get_start_end_dates(years, start, end)
#         # df, company = get_ticker(ticker, _start, _end)

#         data_dic[key] = [df, company]

#     return data_dic
