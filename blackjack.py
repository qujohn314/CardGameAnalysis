from typing import List

from deck import *
from dataclasses import dataclass
from enum import Enum
import typing

CARD_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
               "A": 11}


class Action(Enum):
    STAND = 1
    HIT = 2
    DOUBLE_DOWN = 3
    SPLIT = 4


@dataclass
class Rules:
    num_deck: int = 1
    soft17: bool = False
    split_aces: bool = True
    double_after_split: bool = True
    payout: float = 1.5
    insurance: bool = True
    insurance_payout: float = 2.0
    max_hands_in_play: int = 1
    max_bet: int = 1000
    min_bet: int = 25


def get_hand_value(cards: List[Card]) -> int:
    total = 0
    for card in cards:
        if card.rank == "A" and total + CARD_VALUES[card.rank] > 21:
            total += 1
        else:
            total += CARD_VALUES[card.rank]

    return total


class Agent:
    def __init__(self, bankroll: int, rules: Rules):
        self.bankroll = bankroll
        self.rules = rules

    def buy_insurance(self):
        raise NotImplementedError

    def action(self, agent_cards: List[Card], dealer_card: Card, other_visible_cards: List[Card]) -> int:
        raise NotImplementedError


class NaiveOptimum(Agent):
    def __init__(self, bankroll: int, rules: Rules):
        super().__init__(bankroll, rules)
        pass

    def buy_insurance(self):
        return False

    def action(self, agent_cards: List[Card], dealer_card: Card, other_visible_cards: List[Card]) -> int:
        agent_hand_value = get_hand_value(agent_cards)
        dealer_value = CARD_VALUES[dealer_card]


class SimpleHighLow(Agent):
    def __init__(self, bankroll, rules):
        super().__init__(bankroll, rules)
        pass

    def buy_insurance(self):
        pass

    def action(self, agent_cards: List[Card], dealer_card: Card, other_visible_cards: List[Card]) -> int:
        pass


class HighLow(Agent):
    def __init__(self, bankroll, rules):
        super().__init__(bankroll, rules)
        pass

    def action(self, agent_cards: List[Card], dealer_card: Card, other_visible_cards: List[Card]) -> int:
        pass


class BlackJack:
    def __int__(self, rules, agents):
        self.rules = rules
        self.agents = agents

    def simulate_game(self, timesteps=50):
        for t in timesteps:
            pass
