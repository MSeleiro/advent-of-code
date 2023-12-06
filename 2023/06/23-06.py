#
#   --- Day 6: Wait For It ---
#

import re


def extract_nums(s: str) -> list[int]:
    return [int(n) for n in re.findall(r'\d+', s)]


def part1(lines: list[str]) -> int:
    time = extract_nums(lines[0])
    record = extract_nums(lines[1])

    mult = 1
    for t, r in zip(time, record):
        milis = list(range(t + 1))
        beaten = 0
        for hold, race in zip(milis, reversed(milis)):
            m = hold * race
            if m > r:
                beaten += 1

        mult *= beaten

    return mult


def part2(lines: list[str]) -> int:
    time = extract_nums(lines[0].replace(" ", ""))[0]
    record = extract_nums(lines[1].replace(" ", ""))[0]

    milis = list(range(time + 1))
    beaten = 0
    for hold, race in zip(milis, reversed(milis)):
        m = hold * race
        if m > record:
            beaten += 1

    return beaten


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))