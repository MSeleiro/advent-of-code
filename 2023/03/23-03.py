#
#   --- Day 3: Gear Ratios ---
#

import re

def part1(lines: list[str]) -> int:
    number_coords = []
    symbol_idx = []
    for i, line in enumerate(lines):
        number_coords.extend((i, match) for match in re.finditer(r'\d+', line))
        symbol_idx.extend((i, match.start()) for match in re.finditer(r'[^0123456789.\n]', line))
    
    sum = 0
    for i, j in symbol_idx:
        for _, number in filter(lambda x: i-1 <= x[0] <= i+1 , number_coords):
            j_low, j_high = number.span()
            if j_low - 1 <= j <= j_high:
                sum += int(number.group())
                    
    return sum


def part2(lines: list[str]) -> int:
    number_coords = []
    symbol_idx = []
    for i, line in enumerate(lines):
        number_coords.extend((i, match) for match in re.finditer(r'\d+', line))
        symbol_idx.extend((i, match.start()) for match in re.finditer(r'\*', line))
    
    sum = 0
    for i, j in symbol_idx:
        ratio = []
        for _, number in filter(lambda x: i-1 <= x[0] <= i+1 , number_coords):
            j_low, j_high = number.span()
            if j_low - 1 <= j <= j_high:
                ratio.append(int(number.group()))

        if len(ratio) == 2:
            sum += ratio[0] * ratio[1]

    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))