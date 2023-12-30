import random


SUITES = {"S","H","C","D"}
RANKS = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"}

class Card:
    def __init__(self, rank, suite):
        assert rank in RANKS or rank == "Joker"
        assert suite in SUITES or suite == "Joker"

        self.rank = rank
        self.suite = suite

    def __str__(self):
        return self.rank + self.suite

class Deck:
    def __init__(self, jokers=False):
        self.deck = []
        self.shuffle(jokers)

    def shuffle(self, jokers=False):
        for r in RANKS:
            for s in SUITES:
                self.deck.append(Card(r,s))

        if jokers:
            self.deck.append(Card("Joker","Joker"))

        random.shuffle(self.deck)
        return self.deck

    def draw(self):
        return self.deck.pop(-1)

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        outstr = ""
        for card in self.deck:
            outstr += card.__str__() + " "

        return outstr



