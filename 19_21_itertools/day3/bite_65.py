import itertools
import requests
import os
import urllib.request

## Download file from internet:
## Method 1:
#url = 'http://bit.ly/2iQ3dlZ'
#r = requests.get(url)
#with open('dictionary.txt', 'wb') as f:
#   f.write(r.content)

## Method 2:
#DICTIONARY = os.path.join(os.getcwd(), 'dictionary.txt')
#urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


DICTIONARY = os.path.join(os.getcwd(), 'dictionary.txt')
with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

## Here is the solution:
#def get_possible_dict_words(draw):
#    """
#    Get all possible words from a draw (list of letters) which are valid
#    dictionary words. Use _get_permutations_draw and provided dictionary
#    """
#    permutations = [''.join(word).lower() for word in
#                    _get_permutations_draw(draw)]
#    return set(permutations) & set(dictionary)
#
#
#def _get_permutations_draw(draw):
#    """
#    Helper to get all permutations of a draw (list of letters), hint:
#    use itertools.permutations (order of letters matters)
#    """
#    for i in range(1, 8):
#        yield from list(itertools.permutations(draw, i))

def get_possible_dict_words(draw):
    """
    Get all possible words from a draw (list of letters) which are valid
    dictionary words. Use _get_permutations_draw and provided dictionary
    """
    possible_words = _get_permutations_draw(draw)
    words = []
    for word in possible_words:
        if word in dictionary:
            words.append(word)
    return set(words)


def _get_permutations_draw(draw):
    """
    Helper to get all permutations of a draw (list of letters), hint:
    use itertools.permutations (order of letters matters)
    """
    for n in range(2, len(draw)+1):
        for word in itertools.permutations(draw, n):
            yield ''.join(word).lower()

draw = ['a', 'p', 'p', 'l', 'e', 'a', 'b']
words = get_possible_dict_words(draw)
print(words)
