import re


def extract_course_times():
    """
    Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']
    """
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    pat = re.compile(r'\d\d:\d\d')
    return pat.findall(flask_course)


def get_all_hashtages_and_links():
    """
    Write a regular expression that returns this list:
        ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    """
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    pat = re.compile(r"""
                     (?:         # Non-capturing parenthesis. Without the
                                 # question mark, the regex inside the
                                 # parathesis will be stored as a group.
                     http\S+     # Capture the link (Non-whitespace)
                     |           # or
                     )           # Closing parathesis
                     (?:#\w+)
                     """, re.VERBOSE)
    return pat.findall(tweet)

print(get_all_hashtages_and_links())


def match_first_paragraph():
    """
    Write a regular expression that returns 'pybites != greedy'
    """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    pat = re.compile(r'<p>(.+?)</p>')
    return pat.search(html).group(1)
