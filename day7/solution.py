from dataclasses import dataclass
from collections import defaultdict
import functools
from utils import file_into_list, file_into_string, test


hand_order = [
        "1111100000000",
        "2111000000000",
        "2210000000000",
        "3110000000000",
        "3200000000000",
        "4100000000000",
        "5000000000000"
    ]

@functools.total_ordering
class Hand:

    card_types = "23456789TJQKA"

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    @classmethod
    def from_str(cls, string):
        cards, bid = string.split()
        return cls(cards, int(bid))

    def label(self):
        counts = { k: 0 for k in self.card_types } 
        for c in self.cards:
            counts[c] = counts[c] + 1
        values = "".join([str(v) for v in sorted(counts.values(), reverse=True)])
        return values

    def __eq__(self, other):
        return self.label() == other.label()

    def __lt__(self, other):
        if hand_order.index(self.label()) == hand_order.index(other.label()):
            for i in range(len(self.cards)):
                if self.card_types.index(self.cards[i]) < self.card_types.index(other.cards[i]):
                    return True
                elif self.card_types.index(self.cards[i]) > self.card_types.index(other.cards[i]):
                    return False
                else:
                    continue
        else:
            return hand_order.index(self.label()) < hand_order.index(other.label())


class HandWithJoker(Hand):
    card_types = "J23456789TQKA" # J is now the weakest
    def label(self):
        counts = { k: 0 for k in self.card_types } 
        jokers = 0
        for c in self.cards:
            if c == "J":
                jokers = jokers + 1
            else:
                counts[c] = counts[c] + 1
        values = [str(v) for v in sorted(counts.values(), reverse=True)]
        if jokers > 0:
            for i in range(len(self.card_types)):
                while int(values[i]) < 6 and jokers > 0:
                    values[i] = str(int(values[i]) + 1)
                    jokers = jokers - 1
                if jokers == 0:
                    break
        return "".join(values)


def parse(_inp, hand_class):
    hands = []
    for line in _inp:
        hands.append(hand_class.from_str(line))
    return hands


def part1(_inp):
    hands = sorted(parse(_inp, Hand))
    result = 0
    for i, h in enumerate(hands):
        result = result + h.bid * (i+1)
    return result


test_input = file_into_list("day7/test_input1.txt")
expected = int(file_into_string("day7/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day7/input.txt")
print(part1(real_input))


def part2(_inp):
    hands = sorted(parse(_inp, HandWithJoker))
    result = 0
    for i, h in enumerate(hands):
        result = result + h.bid * (i+1)
    return result

test_input = file_into_list("day7/test_input2.txt")
expected = int(file_into_string("day7/test_output2.txt"))
test(part2, [test_input], [expected])
real_input = file_into_list("day7/input.txt")
print(part2(real_input))
