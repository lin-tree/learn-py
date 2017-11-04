"""
poker hand 规则相关
"""
POINT_TABLE = '23456789TJQKA'

from enum import Enum
class Pattern(Enum):
    """
    牌型及权重
    """
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

_PATTERN_MODE = {
    (True, True): Pattern.STRAIGHT_FLUSH,
    (True, False): Pattern.STRAIGHT,
    (False, True): Pattern.FLUSH,
    '14': Pattern.FOUR_OF_A_KIND,
    '23': Pattern.FULL_HOUSE,
    '113': Pattern.THREE_OF_A_KIND,
    '122': Pattern.TWO_PAIRS,
    '1112': Pattern.PAIR,
    '11111': Pattern.HIGH_CARD
}

class HandCard:
    """
    手牌
    cards: 5张Card构成的list
    """
    def __init__(self, cards):
        self._cards = cards
        self._point_pattern = {}
        is_flush = True
        max_point = min_point = cards[0].point
        for c in cards:
            point = c.point
            max_point = max(max_point, point)
            min_point = min(min_point, point)
            count = self._point_pattern.get(point)
            self._point_pattern[point] = count and count + 1 or 1
            if c.suit != cards[0].suit:
                is_flush = False
        point_mode = ''.join(map(str, sorted(self._point_pattern.values())))
        is_straight = point_mode == '11111' and max_point - min_point == len(cards) - 1

        self._pattern = _PATTERN_MODE.get((is_straight, is_flush)) or _PATTERN_MODE.get(point_mode)
        if self._pattern is None:
            raise Exception('格式不佳')

    def _show(self):
        print('Cards:', str(self))
        print('Pattern', self._pattern)
        # print('Base', self.base_value())

    def base_value(self):
        """
        基本大小（相同牌型的比较用）\n
        点数按照数量从大到小排列\n
        点数相同的按照点数从大到小排列\n
        2C 2S 5S AC 2D \n
        - 3 张 ‘2’(对应point为0)
        - 1 张 'A'(对应point为12)
        - 1 张 '5'(对应point为3)
        
        base_value [0, 12, 3] <- ('2', 'A', '5')
        """
        return sorted(self._point_pattern.keys(), key=lambda x: [self._point_pattern[x], x], reverse=True)

    @property
    def pattern(self):
        return self._pattern

    def __str__(self):
        return ' '.join(map(str, self._cards))

def judge(handcard1, handcard2):
    """
    判断两副手牌的大小\n
    handcard1, handcard2: 两副手牌\n
    return: code, reason\n
    - code: 0表示平局， 1表示前者胜，2表示后者胜利
    - resaon: 原因（牌型或关键牌）
    """
    pattern1, pattern2 = handcard1.pattern, handcard2.pattern
    name1, name2 = pattern1.name, pattern2.name
    if pattern1 == pattern2:
        bv1, bv2 = handcard1.base_value(), handcard2.base_value()
        for i in range(0, len(bv1)):
            if bv1[i] > bv2[i]:
                return 1, '%s: %s > %s' % (name1, POINT_TABLE[bv1[i]], POINT_TABLE[bv2[i]])
            elif bv1[i] < bv2[i]:
                return -1, '%s: %s > %s' % (name2, POINT_TABLE[bv2[i]], POINT_TABLE[bv1[i]])
        return 0, name1
    elif pattern1 > pattern2:
        return 1, '%s > %s' % (name1, name2)
    else:
        return -1, '%s > %s' % (name2, name1)

def _test():
    """
    测试用
    """
    import card
    _TEST_DATA = [
        'TC JC QC KC AC',
        '3C 6C 8C 2C 5C',
        '6C 7C 8S 9C TC',
        '3C 3S 3D 3H 6C',
        'TC TS 4S 4C TD',
        'QC QD QH 4S 6C',
        '3C 3H 4S 4C 6S',
        '3S 3C 4S 5H 6C',
        '3C 5S 9S KC AC'
    ]
    for s in _TEST_DATA:
        hand_card = HandCard(card.parse_handcard(s))
        hand_card._show()
        print('')

if __name__ == '__main__':
    _test()
