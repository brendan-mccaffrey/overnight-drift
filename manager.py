import pickle
import pandas as pd


def save(data, filename):
    with open(filename, "wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load(filename):
    with open(filename, "rb") as handle:
        data = pickle.load(handle)
    return data


# This takes in a dictionary and returns a df
def format(data, name):
    rows = []
    for entry in data:
        for day in entry.keys():
            newrow = [day, entry[day]["open"], entry[day]["close"]]
            rows.append(newrow)

    df = pd.DataFrame(rows)
    df.columns = ["Date", "open", "close"]
    df.set_index("Date", inplace=True)

    print(df[:10])
    save(df, name)

    return df
