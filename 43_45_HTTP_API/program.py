import api


def main():
    print_header()
    keyword = input('What would you like to search: ')
    results = api.get_search_result(keyword)
    print('There are {} matching episodes: '.format(len(results)))
    for i, result in enumerate(results, 1):
        print('{}. {}'.format(i, result.title))


def print_header():
    print('-' * 50)
    print(' ' * 10 + 'Search TalkPythonToMe Podcast')
    print('-' * 50)


if __name__ == '__main__':
    main()
