import api


def main():
    print_header()
    event_loop()


def print_header():
    print('-' * 50)
    print(' ' * 10 + "Search GitHub User's Repo")
    print('-' * 50)


def event_loop():
    user_name = None
    while user_name != 'x':
        user_name = input('Please input the user name: ')
        search_results = api.get_search_result(user_name)
        for i, result in enumerate(search_results, 1):
            print('{}. {}'.format(i, result.get('name')))



if __name__ == '__main__':
    main()
