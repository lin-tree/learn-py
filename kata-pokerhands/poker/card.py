"""
扑克牌的模块
"""
import random

POINT_TABLE = '23456789TJQKA'
SUIT_TABLE = 'CDHS'
READABLE_SUIT = '♣♦♥♠'
READABLE_POINT = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:

    """
    扑克牌的类
    """

    def __init__(self, pattern, suit=None):
        if len(pattern) == 2 and suit is None:
            self._pattern = pattern
            self._set_pattern(pattern)
        elif len(pattern) == 1 == len(suit):
            self._point = POINT_TABLE.index(pattern)
            self._suit = SUIT_TABLE.index(suit)
            self._pattern = pattern + suit
        else:
            raise Exception('参数不佳，使用Card("2C")或Card("2", "C")')

    @property
    def to_s(self):
        """
        显示可读结果
        """
        return '[%s%s]' % (READABLE_SUIT[self._suit], READABLE_POINT[self._point])

    def __str__(self):
        return self.to_s

    def __repr__(self):
        return '<Card %s>' % self._pattern

    @property
    def pattern(self):
        """
        牌样式
        """
        return self._pattern

    @property
    def suit(self):
        """
        牌花色
        """
        return self._suit

    @property
    def point(self):
        """
        牌点数
        """
        return self._point

    def _set_pattern(self, value):
        self._point = POINT_TABLE.index(value[0])
        self._suit = SUIT_TABLE.index(value[1])

_DECK = [Card(point, suit) for point in POINT_TABLE for suit in SUIT_TABLE]

def shuffle():
    """
    洗牌
    """
    random.shuffle(_DECK)

def gen_pair():
    """
    获取两份手牌
    """
    shuffle()
    return _DECK[0:5], _DECK[5:10]

def gen_handcard():
    """
    获取一份手牌
    """
    shuffle()
    return _DECK[0:5]

def parse_handcard(card_str):
    """
    从字符串构建手牌
    """
    return list(map(Card, card_str.split()))

def _test():
    """
    测试用
    """
    pass

if __name__ == '__main__':
    _test()
