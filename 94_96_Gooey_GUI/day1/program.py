import api


def main():
    print("--------------------------------------")
    print("    MOVIE SEARCH APP (CLI EDITION)")
    print("--------------------------------------")
    print()
    mode, value = get_params()
    operation = {
        'd': api.find_movie_by_director,
        'i': api.find_movie_by_imdb_code,
        'k': api.find_movie_by_keyword,
    }
    results = operation[mode](value)

    print('There are {} movies found.'.format(len(results)))
    for r in results:
        print("{} with code {} and director {} has score {}"
              .format(r.title, r.imdb_code, r.director, r.imdb_score))


def get_params():
    print('How do you want to search?')
    mode = input("By [d]irector, [i]mdb code, or [k]eyword? ").strip().lower()

    if mode == 'd':
        director = input("Enter the director's name: ")
        return mode, director
    elif mode == 'i':
        code = input('Enter the IMDB code: ')
        return mode, code
    else:  # mode == 'k'
        keyword = input('Enter your (single) keyword: ')
        return mode, keyword



if __name__ == '__main__':
    main()
