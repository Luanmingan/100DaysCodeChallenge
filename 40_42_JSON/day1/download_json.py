import requests


url = 'https://raw.githubusercontent.com/mikeckennedy/100daysofcode-with-'\
      'python-course/master/days/40-42-json-data/code/mount-data.txt'
json_file = 'mount-data.txt'
r = requests.get(url)
with open(json_file, 'w') as fout:
    fout.write(r.text)
