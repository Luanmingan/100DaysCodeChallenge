import itertools
import time
from collections import OrderedDict


def main():
    lights = OrderedDict([('green', 20), ('yellow', 5), ('red', 20)])
    iter_light = itertools.cycle(lights.keys())
    iter_time = itertools.cycle(lights.values())

    while True:
        print(next(iter_light))
        time.sleep(next(iter_time))


if __name__ == '__main__':
    main()
