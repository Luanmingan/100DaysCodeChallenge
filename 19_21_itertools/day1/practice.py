import itertools
import sys
import time


# number = list(range(1, 11))
# for i in number:
#     print(i)
#
# print('__iter__' in dir(number))
#
# it = iter('string') print(type(it))
# print(next(it))
# print(next(it))


symbols = itertools.cycle('-\|/')

#for symbol in symbols:
#    sys.stdout.write(symbol)
#    sys.stdout.flush()
#    time.sleep(0.1)

while True:
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush()
    time.sleep(0.1)
