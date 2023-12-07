from dataclasses import dataclass
from collections import defaultdict
import functools
from utils import file_into_list, file_into_string, test


card_types = "AKQJT98765432"
hand_lut = {
        "five": "5000000000000",
        "four": "4100000000000",
        "full": "3200000000000",
        "three": "3110000000000",
        "twop": "2210000000000",
        "pair": "2111000000000",
        "high": "1111100000000"
    }   

hand_lut2 = {v: k for k,v in hand_lut.items()}
ordering = list(reversed(hand_lut.keys()))
print(ordering)


@dataclass
@functools.total_ordering
class Hand:
    cards: str
    bid: int

    @classmethod
    def from_str(cls, string):
        cards, bid = string.split()
        return cls(cards, bid)

    @property
    def label(self):
        counts = { k: 0 for k in card_types } 
        for c in self.cards:
            counts[c] = counts[c] + 1
        values = "".join([str(v) for v in sorted(counts.values(), reverse=True)])
        return hand_lut2[values]

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if ordering.index(self.label) == ordering.index(other.label):

        else:
            return ordering.index(self.label) == ordering.index(other.label)



def parse(_inp):
    hands = []
    for line in _inp:
        hands.append(Hand.from_str(line))
    return hands


def part1(_inp):
    hands = sorted(parse(_inp))
    for h in hands:
        print(h)
        


test_input = file_into_list("day7/test_input1.txt")
expected = int(file_into_string("day7/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day7/input.txt")
print(part1(real_input))


def part2(_inp):
    pass

#test_input = file_into_list("day7/test_input2.txt")
#expected = int(file_into_string("day7/test_output2.txt"))
#test(part2, [test_input], [expected])
#real_input = file_into_list("day7/input.txt")
#print(part2(real_input))
