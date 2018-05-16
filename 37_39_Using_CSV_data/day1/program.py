import research


def main():
    print("Weather research for Seattle, 2014-2015")
    print()

    # Initialize the data
    research.init()

    print("The hotest 5 days:")
    days = research.hot_days()
    for i, d in enumerate(days[0:5]):
        print("{}. {} F on {}".format(i+1, d.actual_max_temp, d.date))

    print("The coldest 5 days:")

    days = research.cold_days()
    for i, d in enumerate(days[0:5]):
        print("{}. {} F on {}".format(i+1, d.actual_max_temp, d.date))

    print("The wettest 5 days:")
    days = research.wet_days()
    for i, d in enumerate(days[0:5]):
        print("{}. {} inches rain on {}"
              .format(i+1, d.actual_precipitation, d.date))


if __name__ == '__main__':
    main()
