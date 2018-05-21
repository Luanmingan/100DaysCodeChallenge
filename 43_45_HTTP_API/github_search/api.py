import requests
from collections import namedtuple


def get_search_result(user_name):
    url = 'https://api.github.com/users/{}/repos'.format(user_name)
    r = requests.get(url)
    r.raise_for_status()
    search_results = r.json()

    return search_results
