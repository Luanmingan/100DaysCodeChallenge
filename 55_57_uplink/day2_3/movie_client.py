import uplink
import requests
from uplink_helper import raise_for_status

base_url = 'http://movie_service.talkpython.fm/'


@raise_for_status
class MovieClient(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url=base_url)

    @uplink.get('api/search/{keyword}')
    def entry_by_keyword(self, keyword) -> requests.models.Response:
        """ Get all movies searched by keyword """

    @uplink.get('api/director/{director_name}')
    def entry_by_director(self, director_name) -> requests.models.Response:
        """ Get all movies searched by director name """

    @uplink.get('api/movie/{imdb_number}')
    def entry_by_imdb(self, imdb_number) -> requests.models.Response:
        """ Get all movies searched by imdb_number """
