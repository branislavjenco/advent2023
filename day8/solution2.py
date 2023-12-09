from dataclasses import dataclass
from collections import defaultdict
import functools
from utils import file_into_list, file_into_string, test


@dataclass
class Node:
    id: str
    next: list




def parse(_inp):
    directions = _inp[0]
    nodes = []
    for line in _inp[2:]:
        id, next = line.split(" = ")
        n = Node(id, next[1:-1].split(", "))
        nodes.append(n)
    return nodes


def part1(_inp):
    directions, nodes = parse(_inp)
    print(directions, nodes)


test_input = file_into_list("day8/test_input1.txt")
test_input11 = file_into_list("day8/test_input11.txt")
expected = int(file_into_string("day8/test_output11.txt"))
expected11 = int(file_into_string("day8/test_output11.txt"))
test(part1, [test_input, test_input11], [expected, expected11])
real_input = file_into_list("day8/input.txt")
print(part1(real_input))


def part2(_inp):
    pass

test_input = file_into_list("day8/test_input2.txt")
expected = int(file_into_string("day8/test_output2.txt"))
test(part2, [test_input], [expected])
real_input = file_into_list("day8/input.txt")
#print(part2(real_input))
