# This lib can be written in a simpler way, but for the sake of practice, I made
# it a little bit longer than needed.


class Roll:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def draw(self, roll):
        if self.name == roll.name:
            return True


# class Rock(Roll):
#     def __init__(self, name, win_name):
#         super().__init__(name)
#         self.win_name = win_name
#
#     def can_defeat(self, roll):
#         if roll.name in self.win_name:
#             return True
#
# class Paper(Roll):
#     def __init__(self, name, win_name):
#         super().__init__(name)
#         self.win_name = win_name
#
#     def can_defeat(self, roll):
#         if roll.name in self.win_name:
#             return True
#
# class Sissor(Roll):
#     def __init__(self, name, win_name):
#         super().__init__(name)
#         self.win_name = win_name
#
#     def can_defeat(self, roll):
#         if roll.name in self.win_name:
#             return True


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name + ' {} points'.format(self.score)


class Rock(Roll):
    def can_defeat(self, roll):
        if roll.name == 'sissor':
            return True


class Sissor(Roll):
    def can_defeat(self, roll):
        if roll.name == 'paper':
            return True


class Paper(Roll):
    def can_defeat(self, roll):
        if roll.name == 'rock':
            return True
