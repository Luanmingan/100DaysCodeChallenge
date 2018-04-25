# import requests


# Download the csv file.
# data = 'https://raw.githubusercontent.com/mikeckennedy/100daysofcode-with
# -python-course/master/days/13-15-text-games/data/battle-table.csv'
# r = requests.get(data)
# with open('battle-table.csv', 'wb') as f:
#    f.write(r.content)



class Roll:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def draw(self, roll):
        if self.name == roll.name:
            return True

    def can_defeat(self, roll, win_team):
        if roll.name in win_team[self.name]:
            return True


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name + ' {} points'.format(self.score)
