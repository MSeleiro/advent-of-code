"""
--- Day 15: Beacon Exclusion Zone ---

--- Part 1 ---
"""
import time
import re


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


def update(c: set, y_to_check: int, height: int, sensor, beacon) -> bool:
    c.update(range(sensor[0] - height, sensor[0] + height + 1))
    if beacon[1] == y_to_check:
        c.remove(beacon[0])
    return False


start_time = time.time()
print(f'Part 1 -> { len(solve(2_000_000, lambda c, y, h, s, b: update(c, y, h, s, b))) }')
print(f'Time -> { (time.time() - start_time) } s')
