#
#  --- Day 9: Mirage Maintenance ---
#

import re
from functools import reduce

def extract_nums(s: str) -> list[int]:
    return [int(n) for n in re.findall(r'-?\d+', s)]


def extrapolate(nums: list[int]) -> int:
    values = []
    values.append((nums[0], nums[-1]))
    while any(n != 0 for n in nums):
        nums = [n2 - n1 for n1, n2 in zip(nums, nums[1:])]
        values.insert(0, (nums[0], nums[-1]))

    return reduce(lambda n1, n2: n2 - n1, [v[0] for v in values]), sum(v[1] for v in values)


def do(lines: list[str]) -> tuple[int, int]:
    firsts, lasts = [], []
    for line in lines:
        nums = extract_nums(line)
        f, l = extrapolate(nums)
        firsts.append(f)
        lasts.append(l)
    
    return sum(lasts), sum(firsts)


with open("input.txt", "r") as f:
    lines = f.readlines()
    p1, p2 = do(lines)
    print(p1)
    print(p2)