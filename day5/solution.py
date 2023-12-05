from dataclasses import dataclass
from collections import defaultdict
from utils import file_into_list, file_into_string, test

@dataclass
class Mapping:
    src: range
    dst: range
    
    @classmethod
    def from_str(cls, string):
        src_start, dst_start, length = [int(s) for s in string.split()]
        src = range(src_start, src_start + length)
        dst = range(dst_start, dst_start + length)
        return cls(src, dst)

    def index(self, inp):
        if inp in src:
            return dst[inp]
        else:
            return inp

@dataclass
class Map:
    mappings: list

    @classmethod
    def from_str(cls, string):
        table = string.split(":")[1] # ignore the header
        mappings = []
        for line in table.strip().split("\n"):
            mappings.append(Mapping.from_str(line))

        return cls(mappings)


def find_next(num, table):
    pass

def parse(_inp):
    almanac = _inp.split("\n\n")
    seeds = [int(s) for s in almanac[0].split(":")[1].strip().split()]
    results = []
    maps = []

    for map_str in almanac[1:]:
        maps.append(Map.from_str(map_str))

    return seeds, maps

        
    

def part1(_inp):
    results = []
    seeds, maps = parse(_inp) 
    for seed in seeds:
        curr = seed
        for m in maps:




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
