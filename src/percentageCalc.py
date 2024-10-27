from collections import Counter
from itertools import combinations, product
from math import factorial

class Calculator:

    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['H', 'D', 'C', 'S']


    def is_straight(self, v):
        return len(v) == len(set(v)) and (
            all(_ in self.values[:5] for _ in v) or all(_ in self.values[1:6] for _ in v) or all(_ in self.values[2:7] for _ in v))


    def get_perc(self, deck, own_cards):                #that not exactly what we see in the lesson, but it uses the code from application 03
        total = 0.0
        three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind, straight, flush, straight_flush, royal_flush =  0, 0, 0, 0, 0, 0, 0, 0
        deck2 = deck.get_new()
        remaining_deck = [card for card in deck2 if card not in own_cards]
        two_cards = list(combinations(remaining_deck, 2))
        hands = [own_cards + list(cards) for cards in two_cards]
        for hand in hands:
            total += 1
            _r, _s, _fl, _fo, _fu = False, False, False, False, False
            for i in range(len(hand)):
                for j in range(i, len(hand)-1):
                    h = [card for card in hand if card != hand[i] and card != hand[j]]
                    v, s = zip(*h)
                    v_count, s_count = Counter(v), Counter(s)
                    if 5 in s_count.values():
                        if self.is_straight(v):
                            if v[-1] == 14:
                                royal_flush += 1 if not _r else 0
                                _r = True
                            straight_flush += 1 if not _s else 0
                            _s = True
                        flush += 1 if not _fl else 0
                        _fl = True
                    if 4 in v_count.values():
                        four_of_a_kind += 1 if not _fo else 0
                        _fo = True
                    if 3 in v_count.values():
                        if 2 in v_count.values():
                            full_house += 1 if not _fu else 0
                            _fu = True

        straight_flush_perc = straight_flush * 100 / total

        flush_perc = flush * 100 / total

        four_of_a_kind_perc = four_of_a_kind * 100 / total

        full_house_perc = full_house * 100 / total

        royal_flush_perc = royal_flush * 100 / total

        return royal_flush_perc, straight_flush_perc, four_of_a_kind_perc, full_house_perc, flush_perc