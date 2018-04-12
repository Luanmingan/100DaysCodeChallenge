"""
A Pomodoro Technique.
How it works:
    1. Set a pomodoro timer (default is 25 min).
    2. When the timer ends, a short break timer (default is 5 min) kicks in.
    3. Go to step 1.
    4. After four pomodoro cycles (step 1 to 3), take a longer break (default
       is 30 min).
"""

from datetime import datetime, time


def main():
    print_header()


def print_header():
    print("-------------------------------------------")
    print("-------------Pomodoro Timer----------------")
    print("-------------------------------------------")


if __name__ == '__main__':
    main()
