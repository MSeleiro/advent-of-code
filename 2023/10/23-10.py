#
#   --- Day 10: Pipe Maze ---
#

pipes = {
    "|" : [(1, 0), (-1, 0)],
    "-" : [(0, 1), (0, -1)],
    "L" : [(0, 1), (-1, 0)],
    "J" : [(0, -1), (-1, 0)],
    "7" : [(0, -1), (1, 0)],
    "F" : [(0, 1), (1, 0)]
}

visited = []

def step(lines: list[str], curr: tuple[int, int], prev: tuple[int, int]) -> tuple:
    moves = pipes[lines[curr[0]][curr[1]]]
    for l, c in moves:
        _new = (curr[0] + l, curr[1] + c)
        if _new != prev:
            return _new, curr
    
    raise RuntimeError("Somehow did not find a match")


def part1(lines: list[str]) -> int:
    s_coord = (0, 0)
    for l, line in enumerate(lines):
        idx = line.find('S')
        if idx != -1:
            s_coord = (l, idx)

    steps = 1
    around = [(s_coord[0] + i, s_coord[1] + j) for i, j in [(1,0), (-1,0), (0,1), (0,-1)]]
    curr = next(filter(lambda p: any(s_coord == (p[0] + l, p[1] + c) for l, c in pipes[lines[p[0]][p[1]]]), around))
    visited.append(curr)
    prev = curr
    while curr != s_coord:
        curr, prev = step(lines, curr, prev)
        visited.append(curr)
        steps += 1
    return int(steps / 2)


def fix_s(lines: list[str]):
    for k, v in pipes.items():
        pipe = True
        for l, c in v:
            coord = (visited[-1][0] + l, visited[-1][1] + c)
            if visited[0] != coord and visited[-2] != coord:
                pipe = False
        if pipe:
            lines[visited[-1][0]] = lines[visited[-1][0]].replace("S", k)


def part2(lines: list[str]) -> int:
    fix_s(lines)

    inside = 0
    skip = None
    for l, line in enumerate(lines):
        out = True
        for c, p in enumerate(line):
            if (l, c) in visited:
                if p == "-":
                    continue
                if p == "F":
                    skip = "7"
                elif p == "L":
                    skip = "J"
                else:
                    if p != skip:
                        out = not out
                    skip = None
            elif not out:
                inside += 1
    return inside


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))