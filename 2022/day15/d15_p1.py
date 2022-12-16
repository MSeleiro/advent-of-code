"""
--- Day 15: Beacon Exclusion Zone ---

--- Part 1 ---
"""
import time


def solve(y_to_check: int, func) -> set:
    y_cardinals = set()
    for line in open("./input.txt").readlines():
        line_coords = []
        temp = ''
        for c in line:
            if c.isdigit() or c == '-':
                temp += c
            else:
                if temp != '':
                    line_coords.append(int(temp))
                temp = ''

        if temp != '':
            line_coords.append(int(temp))
        sensor = (line_coords[0], line_coords[1])
        beacon = (line_coords[2], line_coords[3])
        height = abs(beacon[1] - sensor[1]) + abs(beacon[0] - sensor[0])
        if sensor[1] - height < y_to_check < sensor[1] + height:
            func(y_cardinals, y_to_check, height, sensor, beacon)
    return y_cardinals


def update(c: set, y_to_check: int, height: int, sensor, beacon):
    height2 = height - abs(sensor[1] - y_to_check)
    for i in range(sensor[0] - height2, sensor[0] + height2 + 1):
        c.update({i})
    if beacon[1] == y_to_check:
        c.remove(beacon[0])


start_time = time.time()
print(f'Part 1 -> { len(solve(2_000_000, lambda c, y, h, s, b: update(c, y, h, s, b))) }')
print(f'Time -> { (time.time() - start_time) } s')
