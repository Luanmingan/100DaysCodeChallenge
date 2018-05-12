from website import Website
from crawler import Crawler
import logbook
import sys


def main():
    reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)',
                       False, 'h1', 'div.body_1gnLA')
    crawler = Crawler(reuters)
    crawler.crawl()


def init_logging(filename=None):
    level = logbook.TRACE
    if filename is not None:
        logbook.TimedRotatingFileHandler(
            filename, level=level
        ).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
    msg = 'Logging initialized, level: {}, mode: {}'.format(
        level,
        "stdout mode" if filename is None else "file mode: {}".format(filename)
    )
    logger = logbook.Logger('Startup')


if __name__ == '__main__':
    init_logging()
    main()
