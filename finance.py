import numpy as np
import pandas as pd
import yaml
import yfinance as yf
from easydict import EasyDict as edict
from pandas_datareader import data as pdr

yf.pdr_override()


class StockAnalyer:
    def __init__(self, cfg_name="cfg-quant", cfg_dir="./configs"):
        self.cfg = self.__load__(cfg_name, cfg_dir)

    def __load__(self, filename, config_dir="./configs"):
        with open(f"{config_dir}/{filename}.yaml") as file:
            cfg = yaml.load(file, Loader=yaml.FullLoader)
            cfg = edict(cfg)

        return cfg

    def forward(self):
        pass


def get_start_end_dates(years=5, start=None, end=None):
    if start is None:
        start = dt.today().replace(year=dt.today().year - years)

    if end is None:
        end = dt.today()

    end = end.strftime("%Y-%m-%d")
    start = start.strftime("%Y-%m-%d")

    return start, end
