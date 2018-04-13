"""
A Pomodoro Technique.
How it works:
    1. Set a pomodoro timer (default is 25 min).
    2. When the timer ends, a short break timer (default is 5 min) kicks in.
    3. Go to step 1.
    4. After four pomodoro cycles (step 1 to 3), take a longer break (default
       is 30 min).
"""

from datetime import datetime, timedelta


def main():
    # Default values for the timer. If none, then use the user input.
    work_default = 25
    break_default = 5
    final_break_default = 30

    work_message = "Number of Minutes you want to work: "
    break_message = "Number of Minutes you want to take a break: "
    final_break_message = "Number of Minutes for the final break: "
    print_header()

    work_timespan = get_user_input_time(work_message, work_default)
    break_timespan = get_user_input_time(break_message, break_default)
    work_end_time = datetime.now() + work_timespan
    break_end_time = work_end_time + break_timespan
    final_break_timespan = get_user_input_time(final_break_message,
                                               final_break_default)

    print('It is time to work!')
    for n in range(4):
        while work_end_time > datetime.now():
            continue
        work_end_time = datetime.now() + work_timespan + break_timespan
        print('{} minutes is up. Time to take a break!'
              .format(str(work_timespan.seconds/60)))

        while break_end_time > datetime.now():
            continue
        break_end_time = work_end_time + break_timespan
        print('{} minutes break is over. Now get back to work!'
              .format(str(break_timespan.seconds/60)))

    final_break_end_time = work_end_time + final_break_timespan

    while work_end_time > datetime.now():
        continue
    print('{} minutes is up. Time to take a break!'
          .format(str(work_timespan.seconds/60)))

    while final_break_end_time > datetime.now():
        continue
    print('Project is over.')


def print_header():
    print("-------------------------------------------")
    print("-------------Pomodoro Timer----------------")
    print("-------------------------------------------")
    print()


def get_user_input_time(message, default):
    if default:
        return timedelta(minutes=default)
    if not default:
        user_time = int(input(message))
        return timedelta(minutes=user_time)


if __name__ == '__main__':
    main()
