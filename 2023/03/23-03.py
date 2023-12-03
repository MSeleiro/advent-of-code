#
#   --- Day 3: Gear Ratios ---
#

import re

def part1(lines: list[str]) -> int:
    number_coords = []
    map = []
    for line in lines:
        number_coords.append(list(re.finditer(r'\d+', line)))
        map.append(list(line.strip('\n')))

    symbol_idx = [(i, j) for i, line in enumerate(map) for j, s in enumerate(line) if s != '.' and not s.isdigit()]
    
    sum = 0
    for i, j in symbol_idx:
        for line, number in enumerate(number_coords):
            if i-1 <= line <= i+1:
                for n in number:
                    j_low, j_high = n.span()
                    if j_low - 1 <= j <= j_high:
                        sum += int(n.group())
                    
    return sum


def part2(lines: list[str]) -> int:
    number_coords = []
    map = []
    for line in lines:
        number_coords.append(list(re.finditer(r'\d+', line)))
        map.append(list(line.strip('\n')))

    symbol_idx = [(i, j) for i, line in enumerate(map) for j, s in enumerate(line) if s == '*']
    
    sum = 0
    for i, j in symbol_idx:
        ratio = []
        for line, number in enumerate(number_coords):
            if i-1 <= line <= i+1:
                for n in number:
                    j_low, j_high = n.span()
                    if j_low - 1 <= j <= j_high:
                        ratio.append(int(n.group()))

        if len(ratio) == 2:
            sum += ratio[0] * ratio[1]

    return sum


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))