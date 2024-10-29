import time

import deck
import player
from percentageCalc import Calculator
import random

class Table:
    def __init__(self):
        self.active_players = []
        self.deck = deck.Deck()
        self.playernames = ["SB", "BB", "A", "B", "C", "D", "E", "Dealer"]
        self.players = [player.Player(self.playernames[i], i, 25) for i in range(8)]
        self.community_cards = []
        self.pot = 0
        self.small_blind = 100
        self.big_blind = 200
        self.current_bet = 200
        self.fold = True
        self.calculator = Calculator()

    def play_move(self, current_player, is_preflop):
        ns = time.time_ns()
        his = "fold"
        bet_p = 0
        if not self.fold:
            his = "call" if not self.pot > 200 else "raise"
        action = current_player.get_action(self, is_preflop, his)   #TODO
        if action == "fold":
            current_player.active = False
            self.active_players.remove(current_player)
        elif action == "call":
            self.fold = False
            bet_p = self.current_bet - current_player.betted
            self.bet(current_player, bet_p)
            current_player.betted = self.current_bet
        elif action == "raise":
            self.fold = False
            self.current_bet += self.current_bet
            bet_p = self.current_bet - current_player.betted
            self.bet(current_player, bet_p)
            current_player.betted = self.current_bet

        with open("poker.log", "a") as file:
            file.write(f"{ns}ns | {current_player.name} | {current_player.hole_cards} | {action} {bet_p if action == 'call' or action == 'raise' else ''}\n")

    def bet(self, player, amount):
        player.bet2(amount)
        self.pot += amount

    def play_pre_flop(self):
        with open("poker.log", "w") as file:
            file.write("")
        self.active_players = [p for p in self.players]
        for p in self.players:
            p.hole_cards = self.deck.give_cards(2)
            #print(f"Player: {p.name} has the cards: {p.hole_cards}")

        dealer_index = 0
        self.players[dealer_index].is_dealer = True

        amount_players = len(self.players)
        sb_index = (dealer_index + 1)
        bb_index = (sb_index + 1)
        self.bet(self.players[sb_index],self.small_blind)
        self.players[sb_index].betted = self.small_blind
        self.bet(self.players[bb_index],self.big_blind)
        self.players[bb_index].betted = self.big_blind
        #self.bet(self.players[(bb_index+1)],self.current_bet)
        #self.players[bb_index+1].betted = self.big_blind
        for i in range(amount_players):
            self.play_move(self.players[(bb_index+i)%amount_players], True)
            if len(self.active_players) <= 1:
                break

        #to burn
        self.deck.give_cards(1)
        #and turn
        self.community_cards += self.deck.give_cards(3)
        #print(f"Community Cards: {self.community_cards}")
        self.play_betting_round()

    def play_betting_round(self):
        old_pot = -1
        for current_player in self.active_players:
            ns = time.time_ns()
            #calculate probability
            percentages = self.calculator.get_perc(self.deck, self.community_cards+current_player.hole_cards)
            with open("poker.log", "a") as file:
                file.write(f"{ns}ns | {current_player.name} | {current_player.hole_cards} | {f'R:{percentages[0]}% | S:{percentages[1]}% | K:{percentages[2]}% | H:{percentages[3]}% | F:{percentages[4]}%'}\n")
            self.play_move(current_player, False)
            if len(self.active_players) <= 1:
                break