"""
main
"""
import poker.card as card
import poker.game as game


_TEST_DATA = [
    # [input, winner, reason]
    ['White: TC JC QC KC AC  Blcak: TH JH QH KH AH', 'Tie', 'Pattern.STRAIGHT_FLUSH'],
    ['Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH', 'White', 'Pattern.HIGH_CARD:A>K'],
    ['Black: 2H 4S 4C 2D 4H  White: 2S QS 2S QH 2S', 'Black', 'Pattern.FULL_HOUSE:4>2'],
    ['Pink: 2H 5S 4S 8S 7C  Blue: 8C JS TD 4H QC', 'Blue', 'Pattern.HIGH_CARD:Q>8'],
    ['Pink: 7D 6H 2D 3C 2C  Blue: AS TD AD 4D QH', 'Blue', 'Pattern.PAIR:A>2'],
    ['Pink: 3H KC 2D 2C TH  Blue: 6C KC 4H 8C 2S', 'Pink', 'Pattern.PAIR > Pattern.HIGH_CARD'],
    ['Pink: 6C KC 4S JS 3D  Blue: JH KS 4H QC 9H', 'Tie', 'Pattern.HIGH_CARD'],
    ['Pink: AH 2S 7H 9H 8C  Blue: 8C 3H 3D 8H JS', 'Blue', 'Pattern.TWO_PAIRS > Pattern.HIGH_CARD']
]

def parse_two_handcards(inp):
    """
    将手牌转换
    TODO 用正则取card及进行输入校验
    """
    twos = inp.split('  ')
    h1 = twos[0].split(': ')
    h2 = twos[1].split(': ')
    return [h1[0], card.parse_handcard(h1[1])], [h2[0], card.parse_handcard(h2[1])]

def get_result(cards1, cards2):
    """
    通过手牌获取结果
    """
    code, reason = game.judge(h1[1], h2[1])
    winner = [h2[0], 'Tie', h1[0]][code + 1]
    return winner, reason

def test():
    """
    测试用
    """
    for data in _TEST_DATA:
        winner, reason = get_result(*parse_two_handcards(data[0]))
        print(data[0])
        print(winner, reason)
        assert winner == data[1], "! Winner is %s, expect: %s" % (winner, data[1])
        assert reason == data[2], "! Reason is %s, expect: %s" % (reason, data[2])

if __name__ == '__main__':
    test()
