#
#   --- Day 1: Trebuchet?! ---
#

import re

def part1(lines: list[str]) -> int:
    sum = 0

    for line in lines:
        nums = re.findall(r'\d', line)
        digit = int(nums[0] + nums[-1])
        sum += digit

    return sum


def part2(lines: list[str]) -> int:
    w2n = {
        "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", 
        "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"
    }
    sum = 0
    
    for line in lines:
        regex = f"(?=([0-9]|{'|'.join(w2n.keys())}))"
        matches = re.findall(regex, line)
        nums = [n if n not in w2n else w2n[n] for n in matches]
        digit = int(nums[0] + nums[-1])
        sum += digit

    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
