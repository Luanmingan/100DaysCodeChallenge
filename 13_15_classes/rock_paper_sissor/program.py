from collections import namedtuple
from lib import Rock, Paper, Sissor, Player
import random


def main():
    print_header()
    user_name = get_user_name()
    rolls = build_three_rolls()
    player1 = Player(user_name)
    player2 = Player('computer')
    game_loop(rolls, player1, player2)


def print_header():
    print('-' * 100)
    print(' ' * 40 + 'Rock Paper Sissor')
    print('-' * 100)


def get_user_name():
    user_name = input('What is your name: ')
    return user_name


def build_three_rolls():
    Rolls = namedtuple('roll',
                       'rock gun lightning devil dragon water air paper sponge
                       'wolf tree human snake scissors fire')
    return Rolls(Rock('rock'), Paper('paper'), Sissor('sissor'))


def user_roll_choice(rolls):
    user_choice = input('[R]ock, [P]aper, [S]issor: ').strip().lower()
    if user_choice == 'r':
        return rolls.rock
    elif user_choice == 'p':
        return rolls.paper
    elif user_choice == 's':
        return rolls.sissor


def game_loop(rolls, player1, player2):
    count = 0
    while count < 3:
        player2_roll = random.choice(rolls)
        player1_roll = user_roll_choice(rolls)

        if player1_roll.can_defeat(player2_roll):
            print('{} played {}, {} played {}. Good Job, you scored 1 point!'
                  .format(player2.name, player2_roll.name, player1.name,
                          player1_roll.name))
            player1.score += 1
            count += 1

        elif player1_roll.draw(player2_roll):
            print('{} played {}, {} played {}. It is a draw!'
                  .format(player2.name, player2_roll.name, player1.name,
                          player1_roll.name))

        else:
            print('{} played {}, {} played {}. You lost'
                  .format(player2.name, player2_roll.name, player1.name,
                          player1_roll.name))
            player2.score += 1
            count += 1

    if player1.score > player2.score:
        print('Final score is {} vs {}, {} won!!!'
              .format(player1.score, player2.score, player1.name))
    else:
        print('Final score is {} vs {}, {} won!!!'
              .format(player1.score, player2.score, player2.name))


if __name__ == '__main__':
    main()
