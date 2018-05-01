from itertools import product, permutations, combinations




friends = 'mike bob julian'.split()

print('-----------product function-----------------')

for name in product(friends, repeat=2):
    print(name)

print('----------combinations-----------------')

for name in combinations(friends, 2):
    print(name)

print('----------permutations-----------------')

for name in permutations(friends, 2):
    print(name)
for n in range(2,7):
    print(n)
