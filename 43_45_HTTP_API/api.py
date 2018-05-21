import requests
from collections import namedtuple


Result = namedtuple('Result', 'category, id, url, title, description')


def get_search_result(keyword):
    url = 'http://search.talkpython.fm/api/search?q={}'.format(keyword)
    r = requests.get(url)
    r.raise_for_status()

    search_results = r.json().get('results')

    results = [Result(**r) for r in search_results if
               r.get('category') == 'Episode']
    return results
