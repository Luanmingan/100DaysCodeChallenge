from movie_client import MovieClient


movie_client = MovieClient()


def main():
    val = 'RUN'

    while val:
        command = str(input(
            "Search movies by [1]keyword, [2]director, [3]IMDB: "))
        if command == '1':
            search_by_keyword()
        elif command == '2':
            search_by_director()
        elif command == '3':
            search_by_imdb()
        else:
            print('exiting...')
            break


def search_by_keyword():
    keyword = input('What keyword you want to search: ')
    r = movie_client.entry_by_keyword(keyword)
    r_json = r.json()
    movies = r_json.get('hits')
    for i, movie in enumerate(movies, 1):
        print("{}. {}.".format(i, movie.get('title')))


def search_by_director():
    director_name = input('What director you want to search: ')
    r = movie_client.entry_by_director(director_name)
    r_json = r.json()
    movies = r_json.get('hits')
    for i, movie in enumerate(movies, 1):
        print("{}. {}.".format(i, movie.get('title')))


def search_by_imdb():
    imdb_number = input('What movie you want to search: ')
    r = movie_client.entry_by_imdb(imdb_number)
    movie = r.json()
    try:
        print("The movie you search is --> {}.".format(movie.get('title')))
    except AttributeError as x:
        print('We did not find that movie!')


if __name__ == '__main__':
    main()
