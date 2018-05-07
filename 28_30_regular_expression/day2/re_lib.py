"""
Contains various functions that utilize regular expressions.
"""

import re


def is_allowed_specific_char(string):
    """Check that a string contains only a certain set of characters (in this
    case a-z, A-Z and 0-9)."""
    pat = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(pat.match(string))


def text_match_a(string):
    """Matches a string that has an a followed by zero or more 'b's."""
    pat = re.compile(r'ab*')
    return bool(pat.search(string))


def text_match_b(string):
    """Matches a string that has an a followed by one or more 'b's."""
    pat = re.compile(r'ab+')
    return bool(pat.search(string))


def text_match_c(string):
    """Matches a string that has an a followed by zero or one 'b's."""
    pat = re.compile(r'ab?')
    return bool(pat.search(string))


def text_match_d(string):
    """Matches a string that has an a followed by three 'b's."""
    pat = re.compile(r'ab{3}')
    return bool(pat.search(string))


def text_match_e(string):
    """Matches a string that has an a followed by two to three 'b's."""
    pat = re.compile(r'ab{2,3}')
    return bool(pat.search(string))


def text_match_f(string):
    """Find sequences of lowercase letters joined with a underscore."""
    pat = re.compile(r'^[a-z]+_[a-z]+$')
    return bool(pat.search(string))


def text_match_g(string):
    """Find sequences of one uppercase letter followed by lower case letters."""
    # Another workflow without compile.
    pat = r'[A-Z][a-z]+'
    if re.search(pat, string):
        print('find match!')
    else:
        print('No match!')
