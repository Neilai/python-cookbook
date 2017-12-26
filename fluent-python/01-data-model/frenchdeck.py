import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:

    #for循环和列表结合，利用for循环创建列表
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    #split默认空白
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        #这里这个两重循环要注意 对云每一个 suit分配rank
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    #实现下面两个魔法方法后就可以进行迭代操作
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

# for card in FrenchDeck():
#     print(card)
