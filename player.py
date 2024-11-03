import time

from table2 import Table2
from movements import Movements

class Player:
    #My bank grants loans without interest, so the amount of chips can become negative.
    def __init__(self, name, index, chips_amount):
        self.is_dealer = False
        self.name = name
        self.count_chips = chips_amount
        self.active = True
        self.hole_cards = []
        self.betted = 0
        self.chip = "Casino Royale | 100"
        self.chips = [self.chip for i in range(25)]
        self.movements = Movements()
        self.index = index
        self.table2 = Table2()
        self.pos = int((self.index-2)/2)

    def get_action(self, table, is_preflop, move_before):
        #raise double amount
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ns = time.time_ns()
        if is_preflop:
            position = 0
            paired = False
            str_cards = f"{self.hole_cards[0][1]}{self.hole_cards[1][1]}" if ranks.index(self.hole_cards[0][1]) > ranks.index(self.hole_cards[1][1]) else f"{self.hole_cards[1][1]}{self.hole_cards[0][1]}"
            if self.hole_cards[0][0] == self.hole_cards[1][0] or self.hole_cards[0][1] == self.hole_cards[1][1]:
                paired = True
                position = self.movements.pf_s[str_cards]
            else:
                position = self.movements.pf_uns[str_cards]
            if not self.index > 7-int(position*2.4):
                with open("poker.log", "a") as file:
                    file.write(f"{ns}ns | {self.name} | {self.hole_cards} | {'paired and suited' if paired else 'unpaired'} | {'fold'}\n")
                return "fold"
            with open("poker.log", "a") as file:
                file.write(f"{ns}ns | {self.name} | {self.hole_cards} | {'paired and suited' if paired else 'unpaired'} | {'playable '+self.movements.colors[position]}\n")
            try:
                pos2 = self.table2.dictionary[str_cards]
            except KeyError:
                return "fold"

            return self.table2.test(self.pos, move_before, pos2)

        current_bet = table.current_bet
        return "call"

    def bet2(self, amount):
        self.count_chips -= amount
        self.chips = [self.chip for i in range(max(0, self.count_chips))]