import api
from gooey import GooeyParser, Gooey


@Gooey(program_name='Movie Search App',
       program_description="Search Talk Python's demo data for movies")
def main():
    print("--------------------------------------")
    print("    MOVIE SEARCH APP (GUI EDITION)")
    print("--------------------------------------")
    print()
    mode, value = get_params()
    operation = {
        'Director': api.find_movie_by_director,
        'IMDB Code': api.find_movie_by_imdb_code,
        'Keyword': api.find_movie_by_keyword,
    }
    results = operation[mode](value)

    print('There are {} movies found.'.format(len(results)))
    for r in results:
        print("{} with code {} and director {} has score {}"
              .format(r.title, r.imdb_code, r.director, r.imdb_score))


def get_params():
    parser = GooeyParser()
    parser.add_argument('search_term', help='The search term')
    parser.add_argument(
        dest='mode',
        widget='Dropdown',
        choices=['Director', 'IMDB Code', 'Keyword']
    )
    args = parser.parse_args()
    return args.mode, args.search_term

    #print('How do you want to search?')
    #mode = input("By [d]irector, [i]mdb code, or [k]eyword? ").strip().lower()

    #if mode == 'd':
    #    director = input("Enter the director's name: ")
    #    return mode, director
    #elif mode == 'i':
    #    code = input('Enter the IMDB code: ')
    #    return mode, code
    #else:  # mode == 'k'
    #    keyword = input('Enter your (single) keyword: ')
    #    return mode, keyword


if __name__ == '__main__':
    main()
