from dataclasses import dataclass
from collections import defaultdict
from time import sleep
import functools
from math import lcm
from utils import file_into_list, file_into_string, test


def differences(seq):
    result = []
    for i in range(len(seq) - 1):
        result.append(seq[i+1] - seq[i])
    return result


def extrapolate(histories):
    new_value = histories[-1][-1]
    for i in reversed(range(len(histories)-1)):
        new_value = histories[i][-1] + new_value
    return new_value


def extrapolate_backward(histories):
    new_value = histories[-1][0]
    for i in reversed(range(len(histories)-1)):
        new_value = histories[i][0] - new_value
    return new_value


def get_histories(seq):
    histories = [seq]
    while not all(histories[-1][0] == item for item in histories[-1]):
        histories.append(differences(histories[-1]))
    return histories


def part1(_inp):
    result = 0
    for line in _inp:
        seq = [int(ch) for ch in line.split()]
        histories = get_histories(seq)
        result = result + extrapolate(histories)
    return result


test_input = file_into_list("day9/test_input1.txt")
expected = int(file_into_string("day9/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day9/input.txt")
print(part1(real_input))


def part2(_inp):
    result = 0
    for line in _inp:
        seq = [int(ch) for ch in line.split()]
        histories = get_histories(seq)
        result = result + extrapolate_backward(histories)
    return result


test_input = file_into_list("day9/test_input2.txt")
expected = int(file_into_string("day9/test_output2.txt"))
test(part2, [test_input], [expected])
real_input = file_into_list("day9/input.txt")
print(part2(real_input))
