import requests


url = "http://raw.githubusercontent.com/mikeckennedy/100daysofcode-with-python"\
      "-course/master/days/37-39-csv-data-analsys/weather_csv_demo/data/"\
      "seattle.csv"

r = requests.get(url)
filename = "seattle.csv"
with open(filename, 'wb') as fin:
    fin.write(r.content)

