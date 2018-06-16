from contextlib import contextmanager
import sqlite3


def main():
    name = prompt_for_name()
    with create_db(name) as c:
        c.execute("""
                  CREATE TABLE test_table
                  (name TEXT, address TEXT, number INT)
                  """)
        print('{}.db has been created'.format(name))


@contextmanager
def create_db(name):
    try:
        conn = sqlite3.connect('{}.db'.format(name))
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.close


def prompt_for_name():
    name = input("What would you like to name the database file: ")
    return name


if __name__ == '__main__':
    main()
