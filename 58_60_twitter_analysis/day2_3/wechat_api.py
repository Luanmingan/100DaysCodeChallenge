import itchat
from collections import namedtuple, Counter
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import re
import jieba
import numpy as np
from wordcloud import WordCloud
from PIL import Image


Record = namedtuple(
    'Record',
    'nickname sex province city signature'
)
font_path = '/Library/Fonts/songti.ttc'
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
        signature = friend.get('Signature').strip()
        r = re.compile(r'<span[\s\w="<>/"]+</span>')
        signature = r.sub("", signature)
        record = Record(
            nickname=friend.get('NickName'),
            sex=friend.get('Sex'),
            province=friend.get('Province'),
            city=friend.get('City'),
            signature=signature
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

    def word_cloud(self):
        friends = self.get_friends()
        signatures = [friend.signature for friend in friends
                      if friend.signature]
        text = ''.join(signatures)
        wordlist = jieba.cut(text, cut_all=True)
        word_space_split = " ".join(wordlist)

        coloring = np.array(Image.open("us.jpg"))
        wc = WordCloud(background_color="white", max_words=20000, mask=coloring,
                       max_font_size=30, random_state=42, scale=1,
                       font_path=font_path).generate(word_space_split)

        plt.imshow(wc, interpolation="bilinear")
        plt.axis('off')
        plt.show()
