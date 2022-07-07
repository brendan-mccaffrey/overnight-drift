from datetime import datetime
import yfinance as yf
import pandas as pd
from manager import *

# def trim_recent(df):
#     trim_date = datetime.datetime(2000, 1, 1, 0, 0, 0)

#     for idx, row in df.iterrows():


def yahoo_data(stuff):

    for thing in stuff:
        sector = thing["class"]
        picks = thing["list"]

        for asset in picks:
            print("downloading " + asset["name"])
            data = yf.download(asset["ticker"], start="2022-01-01", interval="1d")

            df = pd.DataFrame(data)

            df = df[["Open", "Close"]]
            df.rename({"Open": "open", "Close": "close"}, axis=1, inplace=True)

            save(df, "data/" + sector + "/" + asset["name"] + ".pickle")

            # print("Testing selecting first open: ", df.iloc[0, 1])
