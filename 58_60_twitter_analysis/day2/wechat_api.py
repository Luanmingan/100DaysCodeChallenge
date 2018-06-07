import itchat
from collections import namedtuple


Record = namedtuple(
    'Record',
    'nickname sex province city signature'
)


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
