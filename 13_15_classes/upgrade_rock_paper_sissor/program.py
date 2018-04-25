from lib import Roll, Player
from collections import defaultdict, namedtuple
import csv
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
                       'rock gun lightning devil dragon water air paper '\
                       'sponge wolf tree human snake scissors fire')
    return Rolls(Roll('rock'), Roll('gun'), Roll('lightning'), Roll('devil'),
                 Roll('dragon'), Roll('water'), Roll('air'), Roll('paper'),
                 Roll('sponge'), Roll('wolf'), Roll('tree'), Roll('human'),
                 Roll('snake'), Roll('scissors'), Roll('fire'))


def user_roll_choice(rolls):
    msg = "[r]ock [g]un [l]ightning [d]evil drag[o]n [w]ater [a]ir [p]aper "\
        "spo[n]ge wol[f] [t]ree [h]uman sna[k]e [s]cissors f[i]re: "
    user_choice = input(msg).strip().lower()
    if user_choice == 'r':
        return rolls.rock
    elif user_choice == 'g':
        return rolls.gun
    elif user_choice == 'l':
        return rolls.lightning
    elif user_choice == 'd':
        return rolls.devil
    elif user_choice == 'o':
        return rolls.dragon
    elif user_choice == 'w':
        return rolls.water
    elif user_choice == 'a':
        return rolls.air
    elif user_choice == 'p':
        return rolls.paper
    elif user_choice == 'n':
        return rolls.sponge
    elif user_choice == 'f':
        return rolls.wolf
    elif user_choice == 't':
        return rolls.tree
    elif user_choice == 'h':
        return rolls.human
    elif user_choice == 'k':
        return rolls.snake
    elif user_choice == 's':
        return rolls.scissors
    elif user_choice == 'i':
        return rolls.fire


def winning_roll():
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        win_team = defaultdict(list)
        for row in reader:
            win_team[row['Attacker'].strip().lower()] = [
                name.strip().lower() for name in row.keys()
                if row[name].strip().lower() == 'win']

    return win_team


def game_loop(rolls, player1, player2):
    win_team = winning_roll()
    count = 0
    while count < 3:
        player2_roll = random.choice(rolls)
        player1_roll = user_roll_choice(rolls)

        if player1_roll.can_defeat(player2_roll, win_team):
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
