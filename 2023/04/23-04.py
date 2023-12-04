#
#   --- Day 4: Scratchcards ---
#

import re

def extract_nums(s: str) -> list[int]:
    return [int(n) for n in re.findall(r'\d+', s)]


def part1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        w, nums = line.split(":")[1].split("|")
        common = set(extract_nums(nums)).intersection(extract_nums(w))
        if len(common):
            sum +=  2 ** (len(common) - 1)
    return sum


def part2(lines: list[str]) -> int:
    copies = [1] * len(lines)
    for idx, line in enumerate(lines):
        w, nums = line.split(":")[1].split("|")
        common = set(extract_nums(nums)).intersection(extract_nums(w))
        num_iter = copies[idx]
        for i in range(len(common)):
            copies[idx + i + 1] += 1 * num_iter
            
    return sum(copies)


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))