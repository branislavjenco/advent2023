from dataclasses import dataclass
from utils import file_into_list, file_into_string, test

@dataclass(frozen=True)
class Pos:
    row: int
    col: int
    
    @classmethod
    def make(cls, row, col):
        # bit of a hacky way to get a custom init for a frozen dataclass
        if row < 0:
            row = 0
        if col < 0:
            col = 0
        return cls(row, col)


@dataclass(frozen=True)
class Area:
    start: Pos
    end: Pos

    @property
    def positions(self):
        positions = set()
        for i in range(self.start.row, self.end.row + 1):
            for j in range(self.start.col, self.end.col + 1):
                positions.add(Pos.make(i, j))
        return positions



@dataclass(frozen=True)
class Number:
    value: int
    area: Area


@dataclass
class Symbol:
    value: str
    pos: Pos

    @property
    def neighbourhood(self):
        return Area(Pos.make(self.pos.row-1, self.pos.col-1), Pos.make(self.pos.row+1, self.pos.col+1))


def overlap(a: Area, b: Area):
    return a.positions & b.positions
   
def parse(_inp):
    numbers = []
    symbols = []
    for row, line in enumerate(_inp):
        line = line + "\n" # for simpler logic
        buf = ""
        for col, ch in enumerate(line):
            if ch.isnumeric():
                buf = buf + ch
            else:
                if len(buf)>0:
                    n = Number(int(buf), Area(Pos.make(row, col-len(buf)), Pos.make(row, col-1)))
                    numbers.append(n)
                    buf = ""
                if ch not in [".", "\n"]:
                    s = Symbol(ch, Pos.make(row, col))
                    symbols.append(s)
    return numbers, symbols


def part1(_inp):
    numbers, symbols = parse(_inp)
    part_numbers = set()
    for num in numbers:
        for sym in symbols:
            if len(overlap(num.area, sym.neighbourhood)) > 0:
                part_numbers.add(num)
    return sum([num.value for num in part_numbers])


test_input = file_into_list("day3/test_input1.txt")
expected = int(file_into_string("day3/test_output1.txt"))
test(part1, [test_input], [expected])
real_input = file_into_list("day3/input.txt")
print(part1(real_input))



def part2(_inp):
    numbers, symbols = parse(_inp)
    result = 0 
    for sym in symbols:
        if sym.value == "*":
            adjacent = []
            for num in numbers:
                if len(overlap(num.area, sym.neighbourhood)) > 0:
                    adjacent.append(num)
            if len(adjacent) == 2:
                result = result + (adjacent[0].value * adjacent[1].value)
    return result


test_input = file_into_list("day3/test_input2.txt")
expected = int(file_into_string("day3/test_output2.txt"))
test(part2, [test_input], [expected])

real_input = file_into_list("day3/input.txt")
print(part2(real_input))
