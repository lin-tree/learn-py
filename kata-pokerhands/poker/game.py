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

class HandCard:
    def __init__(self, cards):
        self._cards = cards
        is_flush = True

        points = []
        max_point = min_point = cards[0].point
        for c in cards:
            max_point = max(max_point, c.point)
            min_point = min(min_point, c.point)
            points.append(c.point)
            if c.suit != cards[0].suit:
                is_flush = False
        is_straight = max_point - min_point == len(cards) - 1

        self._point_pattern = {}
        for p in points:
            c = self._point_pattern.get(p)
            self._point_pattern[p] = c and c + 1 or 1
        point_mode = ''.join(map(str, sorted(self._point_pattern.values())))

        if is_straight:
            self._pattern = is_flush and Pattern.STRAIGHT_FLUSH or Pattern.STRAIGHT
        elif is_flush:
            self._pattern = Pattern.FLUSH
        elif point_mode == '14':
            self._pattern = Pattern.FOUR_OF_A_KIND
        elif point_mode == '23':
            self._pattern = Pattern.FULL_HOUSE
        elif point_mode == '113':
            self._pattern = Pattern.THREE_OF_A_KIND
        elif point_mode == '122':
            self._pattern = Pattern.TWO_PAIRS
        elif point_mode == '1112':
            self._pattern = Pattern.PAIR
        elif point_mode == '11111':
            self._pattern = Pattern.HIGH_CARD
        else:
            raise Exception('格式不佳')

    def _show(self):
        print('Cards:', str(self))
        print('Pattern', self._pattern)
        # print('Base', self.base_value())

    def base_value(self):
        """
        基本大小（相同牌型的比较用）\n
        TC TS 4S 4C TD Pattern.FULL_HOUSE \n
        base_value [8, 2] <- ('10', '4')
        """
        return sorted(self._point_pattern.keys(), key=lambda x: self._point_pattern[x]*10 + x, reverse=True)

    @property
    def pattern(self):
        return self._pattern


    def __str__(self):
        return ' '.join(map(str, self._cards))

def judge(cards1, cards2):
    h1 = HandCard(cards1)
    h2 = HandCard(cards2)
    p1 = h1.pattern.value
    p2 = h2.pattern.value
    if p1 == p2:
        bv1 = h1.base_value()
        bv2 = h2.base_value()
        for i in range(0, len(bv1)):
            if bv1[i] > bv2[i]:
                return 1, '%s:%s>%s' % (str(h1.pattern), POINT_TABLE[bv1[i]], POINT_TABLE[bv2[i]])
            elif bv1[i] < bv2[i]:
                return -1, '%s:%s>%s' % (str(h2.pattern), POINT_TABLE[bv2[i]], POINT_TABLE[bv1[i]])
            else:
                return 0, str(h1.pattern)
    elif p1 > p2:
        return 1, '%s > %s' % (str(h1.pattern), str(h2.pattern))
    else:
        return -1, '%s > %s' % (str(h2.pattern), str(h1.pattern))

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
