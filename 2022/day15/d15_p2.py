"""
--- Day 15: Beacon Exclusion Zone ---

--- Part 2 ---

started at 3_360_000
"""

import time
import re
l_b = 0
u_b = 4_000_000


def solve(y_to_check: int, func) -> set:
    y_cardinals = set()
    for line in open("./input.txt").readlines():
        line_coords = list(map(int, re.findall(r'-?\d+', line)))
        sensor = (line_coords[0], line_coords[1])
        beacon = (line_coords[2], line_coords[3])
        height = abs(beacon[1] - sensor[1]) + abs(beacon[0] - sensor[0])
        if sensor[1] - height < y_to_check < sensor[1] + height:
            height2 = height - abs(sensor[1] - y_to_check)
            if func(y_cardinals, y_to_check, height2, sensor, beacon):
                del y_cardinals
                return set()
    return y_cardinals


def find_missing(lst) -> list:
    return sorted(set(range(lst[0], lst[-1])) - set(lst))


def update(c, h, s) -> bool:
    c.update(range(max(s[0] - h, l_b), min(s[0] + h + 1, u_b + 1)))
    return len(c) == u_b + 1


start_time = time.time()
#                 84%        86%
for y in range(3_379_001, 3_440_000):
    cardinals = solve(y, lambda c, _, h, s, b: update(c, h, s))
    if len(cardinals) != 0:
        sol = find_missing(list(cardinals))[0] * 4_000_000 + y
        print(f'Part 2 -> { sol } with line = { y }')
        break
    if y % 100 == 0:
        print(f'Checkpoint 100 checked, { y } is done. Time elapsed -> { (time.time() - start_time) } seconds')
        start_time = time.time()
