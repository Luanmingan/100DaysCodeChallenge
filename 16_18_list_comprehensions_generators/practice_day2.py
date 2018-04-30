import random


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves', 'julbob pybites',
         'bob belderbos', 'julian sequeira', 'al pacino', 'brad pitt',
         'matt damon', 'brad pitt']


capital_names = [name.title() for name in NAMES]

reversed_names = [' '.join(name.split()[::-1]) for name in capital_names]


def gen_pairs():
    first_names = [name.split()[0].title() for name in capital_names]
    while True:
        first, second = random.sample(first_names, 2)
        yield '{} teams up with {}'.format(first, second)

#    for first in first_names:
#        first_names.remove(first)
#        second = random.choice(first_names)
#        first_names.remove(second)
#        yield '{} teams up with {}'.format(first, second)


def sort_by_surname_desc():
    return sorted([name.split()[1] for name in NAMES], reverse=True)


sorted_list = sort_by_surname_desc()
print(sorted_list)
