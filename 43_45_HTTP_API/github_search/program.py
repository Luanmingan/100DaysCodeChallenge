import api
import requests.exceptions
import platform
import subprocess


def main():
    print_header()
    try:
        user_name = input('Please input the user name: ')
        search_results = api.get_search_result(user_name)
        if not search_results:
            print('No repo is found!')
        else:
            for i, result in enumerate(search_results, 1):
                print('{}. {}'.format(i, result.get('name')))
        select_repo_event_loop(search_results)
    except requests.exceptions.HTTPError:
        print('Error: Search text is required.'.format())

    except Exception as x:
        print('something wrong: {}'.format(x))


def print_header():
    print('-' * 50)
    print(' ' * 10 + "Search GitHub User's Repo")
    print('-' * 50)


def fire_browser(url):
    print('Opening browser for the selected repo')
    if platform.system() == 'Darwin':
        subprocess.call(['open', url])
    elif platform.system() == 'Windows':
        subprocess.call(['start', url])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', url])
    else:
        print("We don't suport your os: " + platform.system())


def select_repo_event_loop(search_results):
    while True:
        selected_number = input('What repo do you want to check out? ')
        if selected_number == 'x':
            print('Exiting...')
            break
        else:
            try:
                selected_url = search_results[
                    int(selected_number) - 1].get('html_url')
                fire_browser(selected_url)
            except IndexError:
                print('Please use a valid number!')
            except ValueError:
                print('Please input numbers.')
            except Exception as x:
                print('Error: {}'.format(type(x)))


if __name__ == '__main__':
    main()
