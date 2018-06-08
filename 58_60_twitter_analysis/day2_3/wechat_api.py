import itchat
from collections import namedtuple, Counter
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt


Record = namedtuple(
    'Record',
    'nickname sex province city signature'
)
font_path = '/home/yang/.local/share/fonts/wqy-zenhei.ttc'
prop = FontProperties(fname=font_path)
plt.figure(figsize=(20, 20))


class Wechat():
    def __init__(self):
        self.friends = None

    @staticmethod
    def login(auto=False):
        if auto:
            itchat.auto_login()
        else:
            itchat.login()

    def get_friends(self):
        self.friends = itchat.get_friends(update=True)
        return [self._parse_row(friend) for friend in self.friends]

    def _parse_row(self, friend):
        record = Record(
            nickname=friend.get('NickName'),
            sex=friend.get('Sex'),
            province=friend.get('Province'),
            city=friend.get('City'),
            signature=friend.get('Signature')
        )
        return record

    def plot_gender(self, show_unknown=False):
        num_of_male = 0
        num_of_female = 0
        num_of_other = 0
        for friend in self.get_friends():
            if friend.sex == 1:
                num_of_male += 1
            elif friend.sex == 2:
                num_of_female += 1
            else:
                num_of_other += 1
        if show_unknown:
            x = ['Male', 'Female', 'Other']
            y = [num_of_male, num_of_female, num_of_other]
        else:
            x = ['Male', 'Female']
            y = [num_of_male, num_of_female]
        plt.bar(x, y)
        plt.xlabel('Gender')
        plt.ylabel('Counts')
        plt.title('Gender Distribution')
        plt.show()

    def plot_province(self, n=10, show_unknown=False):
        if show_unknown:
            provinces = [record.province for record in self.get_friends()]
        else:
            provinces = [record.province for record in self.get_friends()
                         if record.province]
        counter = Counter(provinces)
        top_provinces = counter.most_common(n)
        x, y = zip(*top_provinces)

        plt.bar(x, y)
        plt.xticks(fontproperties=prop)
        plt.xlabel('Province')
        plt.ylabel('Counts')
        plt.title('Province Distribution')
        plt.show()

    def plot_city(self, n=15, show_unknown=False):
        if show_unknown:
            cities = [record.city for record in self.get_friends()]
        else:
            cities = [record.city for record in self.get_friends()
                      if record.city]
        counter = Counter(cities)
        top_cities = counter.most_common(n)
        x, y = zip(*top_cities)

        plt.bar(x, y)
        plt.xticks(fontproperties=prop)
        plt.xlabel('City')
        plt.ylabel('Counts')
        plt.title('City Distribution')
        plt.show()
