import os
import csv
from collections import namedtuple


data = []
Record = namedtuple('Record',
                    'country,beer_servings,spirit_servings,wine_servings,'
                    'total_litres_of_pure_alcohol')


def init():
    filename = 'drinks.csv'
    folder = 'data'
    filepath = os.path.abspath(os.path.join(folder, filename))

    with open(filepath) as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    """
    Convert all strings to float or ints.
    """
    row['beer_servings'] = int(row['beer_servings'])
    row['spirit_servings'] = int(row['spirit_servings'])
    row['wine_servings'] = int(row['wine_servings'])
    row['total_litres_of_pure_alcohol'] = float(
        row['total_litres_of_pure_alcohol'])

    record = Record(**row)
    return record


def sort_beer(data):
    return sorted(data, key=lambda r: -r.beer_servings)


def sort_spirit(data):
    return sorted(data, key=lambda r: -r.spirit_servings)


def sort_wine(data):
    return sorted(data, key=lambda r: -r.wine_servings)
