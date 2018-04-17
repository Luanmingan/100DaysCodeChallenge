import requests
from collections import defaultdict, namedtuple, Counter, deque
import csv

# Download the movie data.
# movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
# r = requests.get(movie_data)
# with open('movie.csv', 'wb') as f:
#    f.write(r.content)
#
# Use nametuple to describe a movie so we can access movie attributes.
Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data='movie.csv'):
    """
    Extracts all movies from csv and stores them in a dictionary where keys are
    directors, and values is a list of movies (named tuples)
    """
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    return directors


directors = get_movies_by_director()


print(directors['Christopher Nolan'])
print(type(directors))
print(type(directors['christopher Nolan']))
