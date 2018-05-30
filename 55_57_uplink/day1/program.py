import uplink
from blog_client import BlogClient


def main():
    val = 'RUN'

    while val:
        print("What would you like to do next?")
        val = input('[w]rite a post or [r]ead them?')

        if val == 'w':
            write_post()
        elif val == 'r':
            read_post()


def read_post():
    svc = BlogClient()
    r = svc.all_entries()
    r.raise_for_status()

    posts = r.json()
    for i, p in enumerate(posts, 1):
        print(" {}. [{} views] {}".format(
            i, p.get('view_count'), p.get('title')
        ))

    selected = int(input('Which number to view? '))
    selected_id = posts[selected-1].get('id')
    selected_post = svc.entry_by_id(selected_id)

    r = svc.entry_by_id(selected_id)
    r.raise_for_status()

    selected_post = r.json()


def write_post():
    pass


if __name__ == '__main__':
    main()
