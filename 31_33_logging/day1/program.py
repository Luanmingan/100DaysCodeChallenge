import api
import requests.exceptions
import logbook


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print('There are {} movies found.'.format(len(results)))
        for r in results:
            print("{} with code {} has score {}"
                  .format(r.title, r.imdb_code, r.imdb_score))
    except requests.exceptions.ConnectionError:
        print('Error: Could not find server. Check your network connection.')
    except ValueError:
        print('Error: Your must specify a search term.')
    except Exception as x:
        print("Oh that didn't work!: {}".format(x))


def inti_logging(filename: str = None):
    level = logbook.TRACE



if __name__ == '__main__':
    main()
