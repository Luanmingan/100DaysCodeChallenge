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

    posts = r.json()
    for i, p in enumerate(posts, 1):
        print(" {}. [{} views] {}".format(
            i, p.get('view_count'), p.get('title')
        ))
    print()

    selected = int(input('Which number to view? '))
    selected_id = posts[selected-1].get('id')
    selected_post = svc.entry_by_id(selected_id)

    r = svc.entry_by_id(selected_id)

    selected_post = r.json()
    print("Details for select_post: {}".format(selected_post.get('id')))
    print("Title: " + selected_post.get('title'))
    print("Written: " + selected_post.get('published'))


def write_post():
    svc = BlogClient()

    title = input("Title: ")
    content = input("body contents: ")
    view_count = int(input("view count (int): "))

    r = svc.create_new_entry(title, content, view_count)

    print('\n')
    print("Created new post succesfully: {}".format(r.json().get('id')))
    print('\n')


if __name__ == '__main__':
    main()
