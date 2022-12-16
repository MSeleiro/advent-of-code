"""
--- Day 15: Beacon Exclusion Zone ---

--- Part 2 ---
"""

import time


def find_missing(lst) -> list:
    return sorted(set(range(lst[0], lst[-1])) - set(lst))


start_time = time.time()

lower_bound = 3_900_000
upper_bound = 4_000_000
cardinals: dict[int, set] = {}
for i in range(lower_bound, upper_bound + 1):
    cardinals[i] = set()

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
    for i in range(height):
        if lower_bound <= sensor[1] - i <= upper_bound:
            if sensor[1] - i in cardinals:
                try:
                    cardinals[sensor[1] - i].update(
                        [k for k in range(
                            max(sensor[0] - height + i, lower_bound), min(sensor[0] + height - i + 1, upper_bound + 1)
                        )]
                    )
                except KeyError:
                    pass

                if len(cardinals[sensor[1] - i]) == upper_bound + 1:
                    cardinals[sensor[1] - i].clear()
                    cardinals.pop(sensor[1] - i)

        if lower_bound <= sensor[1] + i <= upper_bound:
            if sensor[1] + i in cardinals:
                try:
                    cardinals[sensor[1] + i].update(
                        [k for k in range(
                            max(sensor[0] - height + i, lower_bound), min(sensor[0] + height - i + 1, upper_bound + 1)
                        )]
                    )
                except KeyError:
                    pass

                if len(cardinals[sensor[1] + i]) == upper_bound - lower_bound + 1:
                    cardinals[sensor[1] + i].clear()
                    cardinals.pop(sensor[1] + i)

y, x = cardinals.popitem()
sol = find_missing(list(x))[0] * 4_000_000 + y

print(f'Part 2 -> { sol } \nTime -> {(time.time() - start_time)} s')
