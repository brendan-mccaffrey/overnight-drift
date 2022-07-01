import requests
import time
import datetime
import pytz
from dateutil.parser import parse
import pickle
from manager import *


# Takes 15 min chart from ftx and
# makes daily open close dict
def process_ftx(data):
    open_price = 0.0
    close_price = 0.0

    market_open = datetime.time(14, 30, 0)  # 1:30pm utc -> 9:30 am EST
    market_close = datetime.time(20, 45, 0)  # 8:00pm utc -> 4:00pm EST

    processed_data = {}
    for entry in data:
        open_time = entry["startTime"].time()

        if open_time == market_open:
            open_price = entry["open"]

        elif open_time == market_close:
            close_price = entry["close"]
            processed_data[entry["startTime"].date()] = {
                "open": open_price,
                "close": close_price,
            }

            open_price = 0.0
            close_price = 0.0

    return processed_data


# pull data from FTX
def pull_ftx(market_name, resolution, start_time, end_time):

    endpoint = (
        "https://ftx.com/api"
        + "/markets/"
        + str(market_name)
        + "/candles?resolution="
        + str(resolution)
        + " &start_time="
        + str(start_time)
        + "&end_time="
        + str(end_time)
    )

    resp = requests.get(endpoint)

    data = resp.json()["result"]

    formatted_data = [
        {k: parse(v, fuzzy=True) if k == "startTime" else v for k, v in entry.items()}
        for entry in data
    ]

    return process_ftx(formatted_data)


def ftx_data(coin):
    today = datetime.datetime(2022, 6, 28, 0, 0, 0)
    start = datetime.datetime(2020, 6, 28, 0, 0, 0)

    delta = datetime.timedelta(days=5)
    end = start + delta

    market = coin + "/USD"
    if coin == "ICP" or coin == "ADA":
        market = coin + "-PERP"

    start_time = time.mktime(start.timetuple())
    end_time = time.mktime(end.timetuple())
    resolution = "900"

    full_data = []
    while end < today:
        result = pull_ftx(market, resolution, start_time, end_time)
        full_data.append(result)
        print("Retreived ", end.date())

        start = end
        end += delta
        start_time = time.mktime(start.timetuple())
        end_time = time.mktime(end.timetuple())

    save(full_data, coin + "_data.pickle")

    return full_data


# format(load("_data.pickle"), "sol.pickle")

# run()
# print(load("btc_data.pickle"))
# data = get_data("BTC/USD")

# process(data)
