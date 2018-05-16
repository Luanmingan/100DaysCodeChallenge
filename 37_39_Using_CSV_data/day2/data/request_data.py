import requests


url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol'\
      '-consumption/drinks.csv'
filename = 'drinks.csv'

r = requests.get(url)
with open(filename, 'wb') as fin:
    fin.write(r.content)
