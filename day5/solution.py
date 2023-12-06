from dataclasses import dataclass
from collections import defaultdict
from utils import file_into_list, file_into_string, test


def parse(_inp):
    almanac = _inp.split("\n\n")
    seeds = almanac[0].split(":")[1].strip().split()
    print(seeds)
    for _map in almanac[1:]:
        table = _map.split(":")[1]
        for line in table.split("\n"):
            pass 
        print(table)
    

def part1(_inp):
    parse(_inp) 
    pass


test_input = file_into_string("day5/test_input1.txt")
expected = int(file_into_string("day5/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day5/input.txt")
print(part1(real_input))


def part2(_inp):
    pass


# test_input = file_into_list("day5/test_input2.txt")
# expected = int(file_into_string("day5/test_output2.txt"))
# test(part2, [test_input], [expected])
# 
# real_input = file_into_list("day5/input.txt")
# print(part2(real_input))
