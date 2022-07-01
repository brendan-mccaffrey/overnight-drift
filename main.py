from manager import *
from ftx import *
from backrun import *
from os.path import exists

from yahoo import yahoo_data

coins = ["BTC", "ETH", "MKR", "SOL", "AVAX", "MATIC", "ICP", "ADA"]
assets = [
    {"name": "S&P500", "ticker": "SPY"},
    {"name": "NASDAQ", "ticker": "^IXIC"},
    {"name": "Gold", "ticker": "GLD"},
    {"name": "Water", "ticker": "CGW"},
    {"name": "Energy", "ticker": "XLE"},
    {"name": "Healthcare", "ticker": "XLV"},
    {"name": "Dow", "ticker": "DJI"},
    {"name": "Vol", "ticker": "VIX"},
]


def run_ftx_data():
    for coin in coins:
        # if raw data exists just load it, else make it
        if not exists(coin + "_data.pickle"):
            raw_data = ftx_data(coin)
        else:
            raw_data = load(coin + "_data.pickle")

        data = format(raw_data, "data/crypto/" + coin + ".pickle")


def test_fees_crypto(coins, fee):
    for asset in coins:
        data = load("data/crypto/" + asset + ".pickle")
        df = backtest_fee(data, fee)
        chart(df, asset + " Strategy with " + str(fee * 100.0) + "% Fee")
        save(df, "fee-tests/crypto/" + asset + ".pickle")


def test_fees_trad(assets, fee):
    for asset in assets:
        data = load("data/assets/" + asset["name"] + ".pickle")
        df = backtest_fee(data, fee)
        chart(df, asset["name"] + " Strategy with " + str(fee * 100.0) + "% Fee")
        save(df, "fee-tests/assets-new/" + asset["name"] + ".pickle")


def run_yahoo_data():
    yahoo_data(assets)


# run_yahoo_data()
test_fees_trad(assets, 0.000013)
# test_fees_crypto(coins, 0.0001)
