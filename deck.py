import random

class Deck:
    def __init__(self):
        self.cards = []
        self.create_new()
        self.shuffle()

    def create_new(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [[ suit, rank] for suit in suits for rank in ranks]

    def get_new(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return[[suit, rank] for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def give_cards(self, count):
        if count > len(self.cards):
            raise ValueError("Not enough cards in deck")
        dealt_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return dealt_cards