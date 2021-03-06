import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = [
            Card(s, v)
            for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        ]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards > 1):
            return self.cards.pop()

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     self.x = -1
    #     if self.x < len(self.cards):
    #         self.x += 1
    #         return self.x
    #     else:
    #         raise StopIteration

            

if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    for x in d.cards:
        print(x)

