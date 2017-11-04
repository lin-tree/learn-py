# Kata Poker Hands

> From http://codingdojo.org/kata/PokerHands/
>
> 一个扑克牌牌型判断的小(da)练习

```plain
|-- main.py
`-- poker
    |-- card.py
    `-- game.py

```

## 核心逻辑

1. 在`poker.game`初始化`HandCard`时识别牌型并保存：  
    1. 遍历`cards`:
        - 判断是否同花色
        - 求出最大最小点数
        - 通过`dict`统计点数，以`{point:count}`格式记录在`_point_pattern`
    2. 处理`_point_pattern`，将其转换成点数牌型特征码`point_mode`：
        - `'11111'`表示所有点数都是不同的牌
        - `'113'`表示有三张同一点数的牌，剩下两张不同（即Three of a kind）
        - ......
    3. 根据最大最小值结合`point_mode`判断牌型是否是一个顺子
    4. 结合是否顺子，是否同花色及`point_mode`判断出具体牌型
2. 在`judge`的时候，根据`base_value`判断相同牌型的大小。
    - `HandCard#base_value()`将牌中点数按照数量从大到小排列，若数量相同，按照点数从大到小排列。这样的顺序刚好是牌型时两组牌按照点数比较大小的顺序。
3. 若不需要得到具体的哪个点数获胜，py里只需要简单的数组比较就行，这里为了知道是哪张牌导致的胜利，进行手动循环挨个儿比较。

## TODO

- 添加注释，重构代码
- 通过正则添加输入校验
- 添加更多测试数据
