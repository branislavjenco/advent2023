from dataclasses import dataclass
from utils import file_into_list, file_into_string, test


@dataclass
class BagConfig:
    max_red: int
    max_green: int
    max_blue: int
    

@dataclass
class Set:
    red: int
    green: int
    blue: int

    def power(self):
        return self.red * self.green * self.blue

    @classmethod
    def from_string(cls, string):
        red = 0
        green = 0
        blue = 0
        parts = string.split(",")
        for part in parts:
            part = part.strip()
            parts = part.split(" ")
            if parts[1] == "red":
                red = int(parts[0])
            elif parts[1] == "green":
                green = int(parts[0])
            elif parts[1] == "blue":
                blue = int(parts[0])
        return cls(red, green, blue)

@dataclass
class Game:
    id: int
    sets: list

    def fewest_cubes(self):
        red = max([_set.red for _set in self.sets])
        green = max([_set.green for _set in self.sets])
        blue = max([_set.blue for _set in self.sets])
        return Set(red, green, blue).power()

    def is_possible(self, bag_config: BagConfig):
        result = True
        for _set in self.sets:
            if _set.red > bag_config.max_red or \
                _set.green > bag_config.max_green or \
                _set.blue > bag_config.max_blue:
                result = False
                break
        return result

    @classmethod
    def from_string(cls, string):
        id_string, set_strings = string.split(":")
        _, game_id = id_string.split(" ")
        sets = []

        for set_string in set_strings.split(";"):
            set_string = set_string.strip()
            sets.append(Set.from_string(set_string))

        return cls(int(game_id), sets)


def part1(_inp):
    bag_config = BagConfig(12, 13, 14)
    result = 0
    for line in _inp:
        game = Game.from_string(line)
        if game.is_possible(bag_config):
            result = result + game.id
    return result


test_input = file_into_list("day2/test_input1.txt")
expected = int(file_into_string("day2/test_output1.txt"))
test(part1, [test_input], [expected])

real_input = file_into_list("day2/input.txt")
print(part1(real_input))


def part2(_inp):
    result = 0
    for line in _inp:
        game = Game.from_string(line)
        result = result + game.fewest_cubes()
    return result


test_input = file_into_list("day2/test_input2.txt")
expected = int(file_into_string("day2/test_output2.txt"))
test(part2, [test_input], [expected])

real_input = file_into_list("day2/input.txt")
print(part2(real_input))
