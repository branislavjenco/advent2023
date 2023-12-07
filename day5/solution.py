import sys
from dataclasses import dataclass
from collections import defaultdict
from utils import file_into_list, file_into_string, test

@dataclass
class Mapping:
    src: range
    diff: int
    
    @classmethod
    def from_str(cls, string):
        dst_start, src_start, length = [int(s) for s in string.split()]
        src = range(src_start, src_start + length)
        diff = (dst_start - src_start)
        print("diff", dst_start, src_start, diff)
        return cls(src, diff)

    def index(self, inp):
        if inp in self.src:
            return inp + self.diff
        else:
            return inp

    def index_range(self, r):
        print(self.src, r)
        overlap = range(max(self.src[0], r[0]), min(self.src[-1], r[-1])+1)
        print(overlap, len(overlap), self.diff)
        # the problem is that the values outside the overlap still need to be mapped (1 to 1 that is)
        if len(overlap) > 0:
            mapped_overlap = range(overlap[0] + self.diff, overlap[-1] + self.diff + 1) # I feel like there should be +1 here
            print("M", mapped_overlap)
            return mapped_overlap
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
        res = _inp
        for m in self.mappings:
            res = m.index(res)
            print(res)
        return res

    def index_range(self, r):
        result = None
        for m in self.mappings:
            res = m.index_range(r)
            if res:
                result = res
                break
        if not result:
            result = r
            print("M", r)

        return result


def parse(_inp, seed_parser):
    almanac = _inp.split("\n\n")
    seeds = seed_parser(almanac)
    results = []
    maps = []

    for map_str in almanac[1:]:
        maps.append(Map.from_str(map_str))

    return seeds, maps
   
def parse_seeds_1(almanac):
    return [int(s) for s in almanac[0].split(":")[1].strip().split()]

def part1(_inp):
    min_result = sys.maxsize
    seeds, maps = parse(_inp, parse_seeds_1) 
    for seed in seeds:
        print("seed", seed)
        curr = seed
        for m in maps:
            print("m", m)
            curr = m.index(curr)
        print("End", curr)
        if curr < min_result:
            min_result = curr
    return min_result




test_input = file_into_string("day5/test_input1.txt")
expected = int(file_into_string("day5/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_string("day5/input.txt")
print(part1(real_input))


def parse_seeds_2(almanac):
    seeds = [int(s) for s in almanac[0].split(":")[1].strip().split()]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        r = range(seeds[i], seeds[i] + seeds[i+1])
        seed_ranges.append(r)
    return seed_ranges 


def part2(_inp):
    min_result = sys.maxsize
    seed_ranges, maps = parse(_inp, parse_seeds_2) 
    #print("parsed")
    for i, seed_range in enumerate(seed_ranges):
        #print(f"{i}/{len(seed_ranges)}")
        curr = seed_range
        for m in maps:
            curr = m.index_range(curr)
        print("FOO", curr)
        min_curr = min(curr)
        if min_curr < min_result:
            min_result = min_curr

    return min_result


test_input = file_into_string("day5/test_input2.txt")
expected = int(file_into_string("day5/test_output2.txt"))
test(part2, [test_input], [expected])

real_input = file_into_string("day5/input.txt")
#print(part2(real_input))
