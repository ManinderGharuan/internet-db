from os import path
from csv import reader


def top_1mScraper():
    DIR = path.dirname(path.dirname(path.abspath(__file__)))
    FILENAME = path.join(DIR, 'top-1m.csv')

    data = []

    with open(FILENAME) as csvfile:
        read = reader(csvfile)

        for row in read:
            data.append(row[1])

    return data
