import movie_api
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('-' * 50)
    print('                 Movie Search App')
    print('-' * 50)
    print()


def search_event_loop():
    search = ''
    while search != 'x':
        try:
            search = input('What movie do you want to search? ')
            if search != 'x':
                results = movie_api.find_movies(search)
                print('Found {} results.'.format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print('Error: Search text is required')
        except requests.exceptions.ConnectionError as ce:
            print('The internet is down.')
        except requests.exceptions.HTTPError as x:
            print('Unexpected error, Details: {}'.format(x))

    print('exiting...')


if __name__ == '__main__':
    main()
