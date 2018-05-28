import requests


url = "https://www.reddit.com/r/technology/.rss"


def main():
    r = requests.get(url)
    with open('reddit_tech.xml', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    main()
