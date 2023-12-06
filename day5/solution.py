from dataclasses import dataclass
from collections import defaultdict
from utils import file_into_list, file_into_string, test

@dataclass
class Mapping:
    src: range
    diff: int
    
    @classmethod
    def from_str(cls, string):
        src_start, dst_start, length = [int(s) for s in string.split()]
        src = range(src_start, src_start + length)
        diff = (dst_start - src_start)
        return cls(src, diff)

    def index(self, inp):
        print(inp, self.src, self.diff)
        if inp in self.src:
            return inp + self.diff
        else:
            return None

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

    def index(self, _inp):
        result = None
        for m in self.mappings:
            res = m.index(_inp)
            if res:
                result = res
                break
        if not result:
            result = _inp
        return result

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
            print(curr)
            curr = m.index(curr)
        results.append(curr)
    print(results)
    return min(results)




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
