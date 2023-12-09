from dataclasses import dataclass
from collections import defaultdict
from time import sleep
import functools
from math import lcm
from utils import file_into_list, file_into_string, test


@dataclass
class Node:
    id: str
    next: list

def parse(_inp):
    directions = _inp[0]
    nodes = {}
    for line in _inp[2:]:
        _id, _next = line.split(" = ")
        n = Node(_id, _next[1:-1].split(", "))
        nodes[_id] = n 
    return directions, nodes

def step(start_node, direction, nodes):
    if direction == "L":
        return nodes[start_node].next[0]
    elif direction == "R":
        return nodes[start_node].next[1]

def traverse(start, directions, nodes, end_condition):
    steps = 0
    prev_node = start
    while True:
        direction = directions[steps % len(directions)]
        node = step(prev_node, direction, nodes)
        steps = steps + 1
        if end_condition(node):
            break
        prev_node = node
    return steps

    
def part1(_inp):
    directions, nodes = parse(_inp)
    return traverse("AAA", directions, nodes, lambda n: n == "ZZZ")



test_input = file_into_list("day8/test_input1.txt")
test_input11 = file_into_list("day8/test_input11.txt")
expected = int(file_into_string("day8/test_output1.txt"))
expected11 = int(file_into_string("day8/test_output11.txt"))
test(part1, [test_input, test_input11], [expected, expected11])
real_input = file_into_list("day8/input.txt")
print(part1(real_input))


def part2(_inp):
    directions, nodes = parse(_inp)
    start_nodes = [n for n in nodes.keys() if n[2] == "A"]
    step_counts = []
    for n in start_nodes:
        steps = traverse(n, directions, nodes, lambda n: n[2] == "Z")
        step_counts.append(steps)
    return lcm(*step_counts)


test_input = file_into_list("day8/test_input2.txt")
expected = int(file_into_string("day8/test_output2.txt"))
test(part2, [test_input], [expected])
real_input = file_into_list("day8/input.txt")
print(part2(real_input))
