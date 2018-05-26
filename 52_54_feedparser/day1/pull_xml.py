import requests


url = "http://store.steampowered.com/feeds/newreleases.xml"


def main():
    r = requests.get(url)
    with open('newreleases.xml', 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    main()
