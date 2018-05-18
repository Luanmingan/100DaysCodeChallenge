import json
import requests
from pprint import pprint

r = requests.get('https://raw.githubusercontent.com/mikeckennedy/100daysofcode-with-python-course/master/days/40-42-json-data/code/mount-data.txt')
data = json.loads(r.text)
