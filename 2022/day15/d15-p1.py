"""
--- Day 15: Beacon Exclusion Zone ---

--- Part 1 ---
"""

import time
start_time = time.time()

y_to_check = 2_000_000
y_cardinals = set()

for line in open("./input.txt").readlines():
    line_coords = []
    temp = ''
    digit = False
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
        height2 = height - abs(sensor[1] - y_to_check)
        for i in range(sensor[0] - height2, sensor[0] + height2 + 1):
            y_cardinals.update({i})
        if beacon[1] == y_to_check:
            y_cardinals.remove(beacon[0])


print(f'Part 1 -> { len(y_cardinals) } \nTime -> { (time.time() - start_time) } s')
