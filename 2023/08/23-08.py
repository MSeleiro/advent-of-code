#
#   --- Day 8: Haunted Wasteland ---
#

from math import lcm

m = {"R" : 1, "L" : 0}


def parse_input(lines: list[str]) -> tuple[list, dict]:
    moves = list(lines[0].rstrip())
    nodes = {}
    for line in lines[2:]:
        m = line.rstrip().split(" = ")
        nodes.update({m[0] : tuple(m[1].strip('()').split(', '))})

    return moves, nodes


def loop(nodes: dict[str, tuple], moves: list, curr, end) -> int:
    steps = 0
    while True:
        step = moves.pop(0)
        curr = nodes[curr][m[step]]
        steps += 1
        if end(curr):
            break
        moves.append(step)

    return steps


def part1(lines: list[str]) -> int:
    moves, nodes = parse_input(lines)
    end_cond = lambda x: x == "ZZZ"
    return loop(nodes, moves, "AAA", end_cond)


def part2(lines: list[str]) -> int:
    moves, nodes = parse_input(lines)   
    curr = list(filter(lambda x: x[2] == 'A', nodes))
    end_cond = lambda x: x[2] == 'Z'
    sizes = [loop(nodes, moves.copy(), pos, end_cond) for pos in curr]
    return lcm(*sizes)


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))