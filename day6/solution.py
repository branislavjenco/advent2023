from dataclasses import dataclass
from collections import defaultdict
from utils import file_into_list, file_into_string, test

@dataclass
class Strategy:
    hold_for: int
    max_time: int

    @property
    def distance(self):
        speed = self.hold_for
        time = self.max_time - self.hold_for
        distance = time * speed
        return distance
    

@dataclass
class Race:
    time: int
    record: int

    def better_strategies(self):
        num = 0
        for i in range(self.time):
            s = Strategy(i, self.time)
            if s.distance > self.record:
                num = num + 1
        return num


def parse(_inp):
    times = [int(t) for t in _inp[0].split(":")[1].split()]
    records = [int(r) for r in _inp[1].split(":")[1].split()]
    races = []
    for i in range(len(times)):
        races.append(Race(times[i], records[i]))
    return races

def part1(_inp):
    races = parse(_inp)
    result = 1
    for r in races:
        result = result * r.better_strategies()
    return result

test_input = file_into_list("day6/test_input1.txt")
expected = int(file_into_string("day6/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day6/input.txt")
print(part1(real_input))


def parse2(_inp):
    times = _inp[0].split(":")[1].split()
    records = _inp[1].split(":")[1].split()
    time = "".join(times)
    record = "".join(records)
    race = Race(int(time), int(record))
    return race

def part2(_inp):
    race = parse2(_inp)
    return race.better_strategies()


test_input = file_into_list("day6/test_input2.txt")
expected = int(file_into_string("day6/test_output2.txt"))
test(part2, [test_input], [expected])
real_input = file_into_list("day6/input.txt")
print(part2(real_input))
