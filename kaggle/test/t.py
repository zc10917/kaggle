import pandas as pd

data = pd.read_csv()
data.a.map

def cal(row):
    p = row.points
    if p >= 95:
        return '3 stars'
    elif p>=85:
        return '2 stars'
    else:
        return '1 star'