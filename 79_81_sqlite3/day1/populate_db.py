import sqlite3


def main():
    enter_details()


def enter_details():
    while True:
        name = input('Enter a name: ')
        address = input('Enter an address: ')
        number = input('Enter a phone number: ')
        info = name, address, number

        with sqlite3.connect("addressbook.db") as connection:
            c = connection.cursor()
            c.execute("INSERT INTO test_table VALUES(?,?,?)", info)
            print('Data inserted to database.\n')

        stop = input("Hit Q to quit.\n")
        if stop.upper() == 'Q':
            break
        else:
            continue


if __name__ == '__main__':
    main()
