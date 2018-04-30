import itertools


def main():
    friends = 'Bob Dante Julian Martin'.split()
    team_size = 2
    order_does_matter = False

    team = friends_teams(friends, team_size, order_does_matter)
    print(team)


def friends_teams(friends, team_size=2, order_does_matter=True):
    if order_does_matter:
        return list(itertools.permutations(friends, team_size))

    if not order_does_matter:
        return list(itertools.combinations(friends, team_size))


if __name__ == '__main__':
    main()
