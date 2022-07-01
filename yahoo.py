import yfinance as yf
import pandas as pd
from manager import *


def yahoo_data(assets):

    for asset in assets:

        print("downloading " + asset["name"])
        data = yf.download(asset["ticker"], period="max", interval="1d")

        df = pd.DataFrame(data)

        df = df[["Open", "Close"]]
        df.rename({"Open": "open", "Close": "close"}, axis=1, inplace=True)

        print(type(df.index[1]))

        print(df.head(5))

        save(df, "data/assets/" + asset["name"] + ".pickle")
