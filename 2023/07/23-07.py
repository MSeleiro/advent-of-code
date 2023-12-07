#
#   --- Day 7: Camel Cards ---
#

import functools
from collections import Counter


def compare_cards(h1: str, h2: str, labels: dict) -> int:
    for c1, c2 in zip(h1, h2):
        if c1 == c2:
            continue
        v1 = int(c1) if c1.isdigit() else labels[c1]
        v2 = int(c2) if c2.isdigit() else labels[c2]
        return int(v1) - int(v2)
    

def compare_counter(c1: Counter, c2: Counter) -> int:
    if len(c1.keys()) < len(c2.keys()) or max(c1.values()) > max(c2.values()):
        return 1
    if len(c1.keys()) > len(c2.keys()) or max(c1.values()) < max(c2.values()):
        return -1
    return 0

def p1_compare_hands(h1: str, h2: str) -> int:
    labels = { "A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10 }
    h1_count, h2_count = Counter(h1[0]), Counter(h2[0])

    res = compare_counter(h1_count, h2_count)
    return res if res != 0 else compare_cards(h1[0], h2[0], labels)


def p2_compare_hands(h1: str, h2: str) -> int:
    labels = { "A" : 14, "K" : 13, "Q" : 12, "J" : 1, "T" : 10 }
    h1_count, h2_count = Counter(h1[0]), Counter(h2[0])

    def updateJ(c: Counter) -> Counter:
        val = c.pop("J")
        if not c:
            c.update({"A" : val})
        else:
            c[max(c, key=c.get)] += val

    if "J" in h1_count:
        updateJ(h1_count)
    if "J" in h2_count:
        updateJ(h2_count)

    res = compare_counter(h1_count, h2_count)
    return res if res != 0 else compare_cards(h1[0], h2[0], labels)


def do(lines: list[str], func) -> int:
    ranks = []
    for line in lines:
        hand, bid = line.rstrip().split(" ")
        bid = int(bid)
        ranks.append((hand, bid))

    ranks.sort(key=functools.cmp_to_key(func))
    
    mult = 0
    for i, hand in enumerate(ranks):
        mult += (i+1) * hand[1]

    return mult


def part1(lines: list[str]) -> int:
    return do(lines, p1_compare_hands)


def part2(lines: list[str]) -> int:
    return do(lines, p2_compare_hands)


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))