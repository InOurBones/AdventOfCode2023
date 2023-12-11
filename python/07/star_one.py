import os
from enum import Enum

input_file = os.path.join(os.path.dirname(__file__), "../../input/day_07.txt")

with open(input_file, "r") as file:
    input = file.read()

class HandTypes(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

    def __lt__(self, other: "HandTypes") -> bool:
        return self.value < other.value
    
    def __gt__(self, other: "HandTypes") -> bool:
        return self.value > other.value

class Card:
    _LETTER_TO_INT = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10
    }

    def __init__(self, card: str):
        self._card = card
        if card in self._LETTER_TO_INT:
            self._value = self._LETTER_TO_INT[card]
        else:
            self._value = int(card)
    
    def __lt__(self, other: "Card") -> bool:
        return self._value < other._value
    
    def __eq__(self, other: "Card") -> bool:
        return self._value == other._value

    def __str__(self) -> str:
        return self._card

class Hand:
    def __init__(self, cards: str, bid: str):
        self._cards = [Card(x) for x in cards]
        self._bid = int(bid)

    @property
    def bid(self) -> int:
        return self._bid

    @property
    def hand_type(self) -> HandTypes:
        tmp = {}
        for x in self._cards:
            x = x._value
            if x not in tmp:
                tmp[x] = 1
            else:
                tmp[x] += 1
                
        # rip match not available in 3.8
        if len(tmp.keys()) == 1:
            return HandTypes.FIVE_KIND
        if 4 in tmp.values():
            return HandTypes.FOUR_KIND
        if [2, 3] == sorted(tmp.values()):
            return HandTypes.FULL_HOUSE
        if 3 in tmp.values():
            return HandTypes.THREE_KIND
        if [1, 2, 2] == sorted(tmp.values()):
            return HandTypes.TWO_PAIR
        if 2 in tmp.values():
            return HandTypes.ONE_PAIR
        return HandTypes.HIGH_CARD

    def __lt__(self, other: "Hand") -> bool:
        if self.hand_type < other.hand_type:
            return True
        
        if self.hand_type > other.hand_type:
            return False
        
        for idx in range(5):
            if self._cards[idx] == other._cards[idx]:
                continue

            return self._cards[idx] < other._cards[idx]
        raise BaseException("shit")
    
    def __str__(self) -> str:
        return "".join([x.__str__() for x in self._cards]) + " " + self.hand_type.__str__()
    
sorted_hands = sorted([Hand(*line.split(" ")) for line in input.split("\n")])
total = 0
for idx, hand in enumerate(sorted_hands):
    total += hand.bid * (idx + 1)
    print(hand)
print(total)