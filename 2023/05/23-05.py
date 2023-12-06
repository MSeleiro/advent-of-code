#
#   --- Day 5: If You Give A Seed A Fertilizer ---
#

import re


def extract_nums(s: str) -> list[int]:
    return [int(n) for n in re.findall(r'\d+', s)]


def new_map(m: dict) -> dict:
    return {k: None for k in m.values()}


def remap_none(maps: dict) -> dict:
    return dict(map(lambda x: (x[0], x[0]) if x[1] is None else (x[0], x[1]), maps.items()))


def part1(lines: list[str]) -> int:
    maps = [{seed: None for seed in extract_nums(lines[0])}]
    curr_map = 0

    for line in lines[3:]:
        if line == '\n':
            continue

        if re.search(r'map', line):
            maps[curr_map] = remap_none(maps[curr_map])
            maps.append(new_map(maps[curr_map]))
            curr_map += 1
        else:
            d, s, l = extract_nums(line)
            for seed in filter(lambda x: s <= x <= s + l, maps[curr_map].keys()):
                maps[curr_map][seed] = d + (seed - s)

    final = remap_none(maps[curr_map])
    return min(final.values())


def map_ranges(mappings, seeds):
    new_ranges = []
    for seed_range in seeds:
        added = False
        for mapping in mappings:
            source_low, source_high = mapping[1], mapping[1] + mapping[2] - 1
            if seed_range[1] < source_low or source_high < seed_range[0]:
                continue

            if seed_range[0] < source_low:
                seeds.append((seed_range[0], source_low - 1))
                seed_range = (source_low, seed_range[1])
            if source_high < seed_range[1]:
                seeds.append((source_high + 1, seed_range[1]))
                seed_range = (seed_range[0], source_high)

            shift = mapping[0] - source_low
            new_ranges.append((seed_range[0] + shift, seed_range[1] + shift))
            added = True
            break

        if not added:
            new_ranges.append(seed_range)
    return new_ranges


def part2(lines: list[str]) -> int:
    range_seeds = extract_nums(lines[0])
    seeds = []
    for i in range(0, len(range_seeds), 2):
        seeds.append((range_seeds[i], range_seeds[i]+range_seeds[i+1] - 1))

    mappings = []
    for line in lines[3:]:
        if line == '\n':
            continue
        if re.search(r'map', line):
            seeds = map_ranges(mappings, seeds)
            mappings = []
        else:
            d, s, l = extract_nums(line)
            mappings.append((d, s, l))

    final = map_ranges(mappings, seeds)
    return min(map(lambda x: x[0], final))


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))