import os
import csv


data = []


def init():
    # this will only work on the current folder.
    # filename = 'seattle.csv'
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'seattle.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            # print(" ROW --> {}".format(row))
            row = parse_row(row)
            print(type(row.get('actual_mean_temp')))


def parse_row(row):
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])
