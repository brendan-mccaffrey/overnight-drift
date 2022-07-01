import datetime
from manager import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def monday(date):
    return date.weekday() == 0


def friday(date):
    return date.weekday() == 4


def weekend(date):
    return date.weekday() > 4


def chart(df, title):
    df = df[
        [
            "hodl",
            "overnight",
            "intraday",
            "weekend",
            "overnight no fee",
            "intraday no fee",
            "weekend no fee",
        ]
    ]
    df.plot(kind="line", figsize=(16, 9))
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value (initial $1,000)")
    plt.title(title)
    plt.show()


def backtest_fee(df, fee):
    fee_factor = (1.0 - fee) ** 2
    print("FEE FACTOR IS " + str(fee_factor))

    # init strategy columns
    df["hodl"] = [1000.0 for row in range(df.shape[0])]
    df["overnight"] = [1000.0 for row in range(df.shape[0])]
    df["intraday"] = [1000.0 for row in range(df.shape[0])]
    df["weekend"] = [1000.0 for row in range(df.shape[0])]

    df["overnight no fee"] = [1000.0 for row in range(df.shape[0])]
    df["intraday no fee"] = [1000.0 for row in range(df.shape[0])]
    df["weekend no fee"] = [1000.0 for row in range(df.shape[0])]

    # init variables
    firstClose = 0.0
    firstFridayClose = 0.0
    lastClose = 0.0
    for date, row in df.iterrows():

        # ignore bad data
        if row["open"] == 0.0 or row["close"] == 0.0:
            row["overnight"] = yesterday["overnight"]
            row["intraday"] = yesterday["intraday"]
            row["weekend"] = yesterday["weekend"]
            row["hodl"] = yesterday["hodl"]
            row["overnight no fee"] = yesterday["overnight no fee"]
            row["intraday no fee"] = yesterday["intraday no fee"]
            row["weekend no fee"] = yesterday["weekend no fee"]

            continue

        # get first friday
        if firstFridayClose == 0.0 and friday(date):
            firstFridayClose = row["close"]

        # get first weekday close
        if firstClose == 0.0:
            if weekend(date):
                continue
            firstClose = row["close"]
            lastClose = firstClose
            yesterday = row
            continue

        # log hodl
        row["hodl"] = 1000.0 * row["close"] / firstClose

        # on weekends hold position in strategies
        if weekend(date):
            row["overnight"] = yesterday["overnight"]
            row["intraday"] = yesterday["intraday"]
            row["weekend"] = yesterday["weekend"]
            row["overnight no fee"] = yesterday["overnight no fee"]
            row["intraday no fee"] = yesterday["intraday no fee"]
            row["weekend no fee"] = yesterday["weekend no fee"]

            continue

        # on weekdays perform trades
        else:

            # intraday buy open sell close
            row["intraday"] = (
                yesterday["intraday"] * row["close"] / row["open"] * fee_factor
            )
            row["intraday no fee"] = (
                yesterday["intraday no fee"] * row["close"] / row["open"]
            )

            # oevrnight buy last close and sell open
            row["overnight"] = (
                yesterday["overnight"] * row["open"] / lastClose * fee_factor
            )
            row["overnight no fee"] = (
                yesterday["overnight no fee"] * row["open"] / lastClose
            )

            # if monday buy last close and sell open
            if monday(date) and firstFridayClose != 0.0:
                row["weekend"] = (
                    yesterday["weekend"] * row["open"] / lastClose * fee_factor
                )
                row["weekend no fee"] = (
                    yesterday["weekend no fee"] * row["open"] / lastClose
                )
            # if not monday hold weekend position
            else:
                row["weekend"] = yesterday["weekend"]
                row["weekend no fee"] = yesterday["weekend no fee"]
            # update lastClose for next iteration
            lastClose = row["close"]

        # store yesterday data for next iteration
        yesterday = row

    return df


# backtest without fee
def backtest_overnight(df):
    df["hodl"] = [1000.0 for row in range(df.shape[0])]
    df["overnight"] = [1000.0 for row in range(df.shape[0])]
    df["intraday"] = [1000.0 for row in range(df.shape[0])]
    df["weekend"] = [1000.0 for row in range(df.shape[0])]
    firstClose = 0.0
    firstFridayClose = 0.0
    lastClose = 0.0

    for date, row in df.iterrows():
        if row["open"] == 0.0 or row["close"] == 0.0:
            row["overnight"] = yesterday["overnight"]
            row["intraday"] = yesterday["intraday"]
            row["weekend"] = yesterday["weekend"]
            row["hodl"] = yesterday["hodl"]
            continue
        if firstFridayClose == 0.0 and friday(date):
            firstFridayClose = row["close"]
        if firstClose == 0.0:
            if weekend(date):
                continue
            firstClose = row["close"]
            lastClose = firstClose
            yesterday = row
            continue
        row["hodl"] = 1000.0 * row["close"] / firstClose
        if weekend(date):
            row["overnight"] = yesterday["overnight"]
            row["intraday"] = yesterday["intraday"]
            row["weekend"] = yesterday["weekend"]
            continue
        else:
            row["intraday"] = yesterday["intraday"] * row["close"] / row["open"]
            row["overnight"] = yesterday["overnight"] * row["open"] / lastClose
            if monday(date) and firstFridayClose != 0.0:
                row["weekend"] = yesterday["weekend"] * row["open"] / lastClose
            else:
                row["weekend"] = yesterday["weekend"]
            lastClose = row["close"]
        yesterday = row
    return df


# backrun()

# data = load("sol.pickle")

# df = backtest_overnight(data)

# chart(df, "SOL Strategies")

# print(df.head(10))

# save(df, "sol-backtest.pickle")


# old backrun script using dictionary
# def backrun():
#     data = load("btc_data.pickle")
#     portfolio = 1.0
#     lastClose = 0.0
#     backtest_data = {}
#     firstDay = 0.0

#     for entry in data:
#         for day in entry.keys():
#             data = entry[day]

#             # santiy check data
#             if data["open"] == 0.0 or data["close"] == 0.0:
#                 continue

#             # for first entry record firstDay open as starting price
#             # and record close price for next iteration
#             if lastClose == 0.0:
#                 firstDay = data["open"]
#                 lastClose = data["close"]
#                 continue

#             # assign last close after computing portfolio change
#             portfolio *= data["open"] / lastClose
#             lastClose = data["close"]

#             backtest_data[day] = {
#                 "open": data["open"],
#                 "close": data["close"],
#                 "overnight_strategy": portfolio,
#                 "HODL": lastClose / firstDay,
#             }

#     for day in backtest_data.keys():
#         print(day, " || ", backtest_data[day])
