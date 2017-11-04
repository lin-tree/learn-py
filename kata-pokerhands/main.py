"""
main
"""
import poker.card as card
import poker.game as game


_TEST_DATA = [
    # [input, winner, reason]
    ['White: TC JC QC KC AC  Black: TH JH QH KH AH', 'Tie', 'STRAIGHT_FLUSH'],
    ['White: 2C 2H 4S 4D 6C  Black: 5H 3H 2H KH 3C', 'White', 'TWO_PAIRS > PAIR'],
    ['White: 2C 2H 4S QD AC  Black: 2D 3H 2S AH KC', 'Black', 'PAIR: K > Q'],
    ['White: 2H 3D 5S 9C KD  Black: 2C 3H 4S 8C AH', 'Black', 'HIGH_CARD: A > K'],
    ['White: 2H 4S 4C 2D 4H  Black: 2S QS 2S QH 2S', 'White', 'FULL_HOUSE: 4 > 2'],
    ['Pink: 2H 5S 4S 8S 7C  Blue: 8C JS TD 4H QC', 'Blue', 'HIGH_CARD: Q > 8'],
    ['Pink: 7D 6H 2D 3C 2C  Blue: AS TD AD 4D QH', 'Blue', 'PAIR: A > 2'],
    ['Pink: 3H KC 2D 2C TH  Blue: 6C KC 4H 8C 2S', 'Pink', 'PAIR > HIGH_CARD'],
    ['Pink: 6C KC 4S JS 3D  Blue: JH KS 4H QC 9H', 'Blue', 'HIGH_CARD: Q > J'],
    ['Pink: AH 2S 7H 9H 8C  Blue: 8C 3H 3D 8H JS', 'Blue', 'TWO_PAIRS > HIGH_CARD']
]

def parse_two_handcards(inp):
    """
    将手牌转换
    TODO 用正则取card及进行输入校验
    """
    input1, input2 = inp.split('  ')
    name1, cardstr1 = input1.split(': ')
    name2, cardstr2 = input2.split(': ')
    return name1, create_handcard(cardstr1), name2, create_handcard(cardstr2)

def create_handcard(cardstr):
    """
    通过字符串创建手牌
    """
    return game.HandCard(card.parse_handcard(cardstr))

def get_result(inp):
    """
    获取结果
    inp: 输入字符串
    """
    name1, hand1, name2, hand2 = parse_two_handcards(inp)
    code, reason = game.judge(hand1, hand2)
    winner = [name2, 'Tie', name1][code + 1]
    return winner, reason

def test():
    """
    测试用
    """
    for data in _TEST_DATA:
        d_input, d_winner, d_reason = data
        winner, reason = get_result(d_input)
        print(d_input)
        print(winner, reason)
        assert winner == d_winner, "! Winner is %s, expect: %s" % (winner, d_winner)
        assert reason == d_reason, "! Reason is %s, expect: %s" % (reason, d_reason)
        print()

if __name__ == '__main__':
    test()
