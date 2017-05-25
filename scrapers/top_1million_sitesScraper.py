from os import path
from csv import reader


def top_1million_sitesScraper():
    DIR = path.dirname(path.abspath(__file__))
    FILENAME = path.join(DIR, 'top-1million-sites.csv')

    data = []

    with open(FILENAME) as csvfile:
        read = reader(csvfile)

        for row in read:
            data.append(row[1])

    return data
