import api
import requests.exceptions
import logbook
import sys


app_log = logbook.Logger('App')


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print('There are {} movies found.'.format(len(results)))
        for r in results:
            print("{} with code {} has score {}"
                  .format(r.title, r.imdb_code, r.imdb_score))
        app_log.trace('Search successful: keyword: {}, {} results.'
                      .format(keyword, len(results)))
    except requests.exceptions.ConnectionError:
        msg = 'Could not find server. Check your network connection.'
        print('Error: ' + msg)
        app_log.warn(msg)
    except ValueError:
        msg = 'Your must specify a search term.'
        print('Error: ' + msg)
        app_log.warn(msg)
    except Exception as x:
        msg = "Oh that didn't work!: {}".format(x)
        print(msg)
        app_log.exception(x)


def init_logging(filename=None):
    level = logbook.TRACE
    if filename:
        logbook.TimedRotatingFileHandler(
            filename, level=level
        ).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mod" if not filename else "file mode: " + filename
    )
    logger = logbook.Logger('Startup')
    logger.notice(msg)


if __name__ == '__main__':
    init_logging('movie-app.log')
    main()
