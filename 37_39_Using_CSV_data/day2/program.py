import research


def main():
    print('Initialize the data.')
    # TODO: initialize csv file.
    research.init()
    print()
    print('-'*50)

    print('Top five countries that consume the most beer:')
    beer_countries = research.sort_beer(research.data)
    for i, record in enumerate(beer_countries[:5], 1):
        print("{}. {} consumes {} servings of beer per year."
              .format(i, record.country, record.beer_servings))
    print()

    print('Top five countries that consume the most spirits:')
    spirit_countries = research.sort_spirit(research.data)
    for i, record in enumerate(spirit_countries[:5], 1):
        print("{}. {} consumes {} servings of spirit per year."
              .format(i, record.country, record.spirit_servings))
    print()

    print('Top five countries that consume the most wine:')
    wine_countries = research.sort_wine(research.data)
    for i, record in enumerate(wine_countries[:5], 1):
        print("{}. {} consumes {} servings of wine per year."
              .format(i, record.country, record.wine_servings))


if __name__ == '__main__':
    main()
