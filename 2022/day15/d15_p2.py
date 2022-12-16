"""
--- Day 15: Beacon Exclusion Zone ---

--- Part 2 ---
"""

import time


def find_missing(lst) -> list:
    return sorted(set(range(lst[0], lst[-1])) - set(lst))


start_time = time.time()

#                 84%        86%
for i in range(3_360_000, 3_440_000):
    d15-p1.solve()
    sol = find_missing(list(x))[0] * 4_000_000 + y
    print(f'Part 2 -> { sol } \nTime -> { (time.time() - start_time) } s')
