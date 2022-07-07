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

assets = [
    {"name": "Microsoft", "ticker": "MSFT"},
    {"name": "Apple", "ticker": "AAPL"},
    {"name": "Robinhood", "ticker": "HOOD"},
    {"name": "US-Crude-Oil", "ticker": "NRGU"},
    {"name": "TQQQ", "ticker": "TQQQ"},
    {"name": "ARK", "ticker": "ARKK"},
    {"name": "Biofuels", "ticker": "FUE"},
    {"name": "RareMetals", "ticker": "REMX"},
    {"name": "DiverseCom", "ticker": "BCI"},
]

inverse = [
    {"name": "Biofuels", "ticker": "FUE"},
]

assets = [
    {
        "class": "stocks",
        "list": [
            {"name": "Apple", "ticker": "AAPL"},
            {"name": "ARK-Innovation", "ticker": "ARKK"},
            {"name": "ARK-Genomics", "ticker": "ARKG"},
            {"name": "ARK-Internet", "ticker": "ARKW"},
            {"name": "NVIDIA", "ticker": "NVDA"},
            {"name": "Crispr", "ticker": "CRSP"},
            {"name": "Piedmont-Lithium", "ticker": "PLL"},
            {"name": "MP-Materials", "ticker": "MP"},
            {"name": "Amazon", "ticker": "AMZN"},
            {"name": "Facebook", "ticker": "META"},
            {"name": "Taiwan-Semiconductor", "ticker": "TSM"},
        ],
    },
    {
        "class": "energy",
        "list": [
            {"name": "Natural-Gas", "ticker": "UNG"},
            {"name": "Brent-Oil", "ticker": "BNO"},
            {"name": "Oil", "ticker": "USO"},
            {"name": "US-Crude-3x", "ticker": "NRGU"},
            {"name": "Energy", "ticker": "DBE"},
        ],
    },
    {
        "class": "commodities",
        "list": [
            {"name": "Coffee", "ticker": "JO"},
            {"name": "Wheat", "ticker": "WEAT"},
            {"name": "Corn", "ticker": "CORN"},
            {"name": "Grains", "ticker": "GRU"},
            {"name": "Sugar", "ticker": "CANE"},
            {"name": "Cocoa", "ticker": "NIB"},
            {"name": "DiverseCom", "ticker": "BCI"},
            {"name": "RareMetals", "ticker": "REMX"},
            {"name": "Nickel", "ticker": "JJN"},
            {"name": "Steel", "ticker": "SLX"},
            {"name": "Copper", "ticker": "JJC"},
        ],
    },
]

assets = [
    {
        "class": "commodities",
        "list": [
            {"name": "Steel", "ticker": "SLX"},
        ],
    },
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


def test_fees_trad(assets, usd_per_share):
    for industry in assets:
        sector = industry["class"]
        items = industry["list"]
        for asset in items:
            data = load("data/" + sector + "/" + asset["name"] + ".pickle")
            df = backtest_fee(data, usd_per_share)
            chart(df, asset["name"] + " Strategy with $" + str(usd_per_share) + " Fee")
            save(df, "fee-tests/" + sector + "/" + asset["name"] + ".pickle")


def run_yahoo_data():
    yahoo_data(assets)


run_yahoo_data()
test_fees_trad(assets, 0.0005)
# test_fees_crypto(coins, 0.0001)

# data = load("data/stocks/NVIDIA.pickle")
# data = data[2000:]
# df = backtest_fee(data, 0.0005)
# chart(df, "Nvidia Strategy with $" + str(0.005) + " Fee")
