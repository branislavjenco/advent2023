from dataclasses import dataclass
from utils import file_into_list, file_into_string, test

@dataclass
class Set:
    red: int
    green: int
    blue: int

    @classmethod
    def from_string(cls, string):
        red = None
        blue = None
        green = None
        parts = string.split(",")
        for part in parts:
            part = part.strip()
            parts = part.split(" ")
            if parts[1] == "red":
                red = int(parts[0])
            elif parts[1] == "blue":
                blue = int(parts[0])
            elif parts[1] == "green":
                green = int(parts[0])
        return cls(red, green, blue)

@dataclass
class Game:
    id: int
    sets: list

    @classmethod
    def from_string(cls, string):
        id_string, set_strings = string.split(":")
        _, game_id = id_string.split(" ")
        sets = []

        for set_string in set_strings.split(";"):
            set_string = set_string.strip()
            sets.append(Set.from_string(set_string))

        return cls(game_id, sets)



def part1(_inp):
    max_red = 12
    max_green = 13
    max_blue = 14
    for line in _inp:
        Game.from_string(line)




test_input = file_into_list("day2/test_input1.txt")
expected = int(file_into_string("day2/test_output1.txt"))
test(part1, [test_input], [expected])

real_input = file_into_list("day2/input.txt")
print(part1(real_input))
