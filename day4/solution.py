from dataclasses import dataclass
from collections import defaultdict
from utils import file_into_list, file_into_string, test


@dataclass
class Card:
    id: int
    winning: set
    have: set

    def matches(self):
        return self.winning & self.have

    def points(self):
        if len(self.matches()) == 0:
            return 0
        else:
            return 2**(len(self.matches())-1)

    @classmethod
    def from_string(cls, string):
        prefix, numbers = string.split(":")
        id = int(prefix.split()[1].strip())
        winning_str, have_str = numbers.split("|")
        winning = set()
        have = set()
        for part in winning_str.strip().split():
            winning.add(int(part))

        for part in have_str.strip().split():
            have.add(int(part))

        return cls(id, winning, have)
            

def part1(_inp):
    result = 0
    for line in _inp:
        card = Card.from_string(line)
        result = result + card.points()
    return result


test_input = file_into_list("day4/test_input1.txt")
expected = int(file_into_string("day4/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day4/input.txt")
print(part1(real_input))


def part2(_inp):
    result = 0
    copies = defaultdict(lambda: 1)
    for line in _inp:
        card = Card.from_string(line)
        for i in range(copies[card.id]):
            for j in range(card.id+1, card.id + len(card.matches()) + 1):
                copies[j] = copies[j] + 1
        result = result + copies[card.id]
    return result


test_input = file_into_list("day4/test_input2.txt")
expected = int(file_into_string("day4/test_output2.txt"))
test(part2, [test_input], [expected])

real_input = file_into_list("day4/input.txt")
print(part2(real_input))
