import re


def extract_course_times():
    """Use re.findall to capture all mm:ss timestamps in a list"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    pat = re.compile(r'\d{2}:\d{2}')
    return pat.findall(flask_course)


def split_on_multiple_chars():
    """Use re.split to split log line by ; , .
       but not on the last ... so list should have len of 4
       (hint check re.split docs for extra switches)"""
    logline = ('2017-11-03T01:00:02;challenge time,regex!.'
               'hope you join ... soon')
    pat = re.compile(r'[;,.]')
    return pat.split(logline, maxsplit=3)


def get_all_hashtags_and_links():
    """Use re.findall to extract the URL and 2 hashtags of this tweet"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    pat = re.compile(r'(?:\#\w+)|(?:http://\S+)')
    return pat.findall(tweet)


def match_first_paragraph():
    """Use re.sub to extract the content of the first paragraph (excl tags)"""
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    pat = re.compile(r'<p>(.+?)</p>')
    return pat.search(html).group(1)


def find_double_words():
    """Use re.search(regex, text).group() to find the double word"""
    text = 'Spain is so nice in the the spring'
    pat = re.compile(r'\b(\w+)\s+\1\b')
    return pat.search(text).group()


def match_ip_v4_address(ip):
    """Use re.match to match an ip v4 address (no need for exact IP ranges)"""
    pat = re.compile(r'(?:\d+.){3}\d+')
    return pat.match(ip)
