from utils import file_into_list, file_into_string, test

def part1(_input):
    result = 0 
    for line in _input:
        curr = ""
        for ch in line:
            if ch.isnumeric():
                curr = curr + ch
                break
        for ch in line[::-1]:
            if ch.isnumeric():
                curr = curr + ch
                break
        result = result + int(curr)
    return result

test_input = file_into_list("day1/test_input1.txt")
expected = int(file_into_string("day1/test_output1.txt"))
test(part1, [test_input], [expected])

real_input = file_into_list("day1/input.txt")
print(part1(real_input))


def part2(_input):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lut = { k:str(v) for k,v in zip(numbers, range(1, 10)) }
    numbers_backwards = [num[::-1] for num in numbers]
    lut_backwards = { k[::-1]:v for k,v in zip(lut.keys(), lut.values()) }

    result = 0 

    def find_first_number(L, nums, table):
        curr = ""
        buf = "" # keep a running buffer of the last couple of characters
        for ch in L:
            if ch.isnumeric():
                return ch
            else:
                buf = buf + ch
                match = False
                for num in nums:
                    if buf.endswith(num):
                        return table[num]
            if len(buf) > 5: # dont need more than 5 as that's the longest 
                buf = buf[1:]

    for line in _input:
        first = find_first_number(line, numbers, lut)
        last = find_first_number(line[::-1], numbers_backwards, lut_backwards)
        curr = first + last
        result = result + int(curr)
    return result



test_input = file_into_list("day1/test_input2.txt")
expected = int(file_into_string("day1/test_output2.txt"))
test(part2, [test_input], [expected])

real_input = file_into_list("day1/input.txt")
print(part2(real_input))
