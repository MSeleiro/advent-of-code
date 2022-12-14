"""
--- Day 14: Regolith Reservoir ---

--- Part 1 ---
"""

import sys

HEIGHT = 200
WIDTH = 600
ROCK = '#'
AIR = '.'
SAND_POINT = '+'
SAND = 'o'

sp = (500, 0)

board = [[AIR for i in range(HEIGHT)] for k in range(WIDTH)]

for line in open("./input.txt").readlines():
    real_line = line.strip("\n")
    rocks = []
    for t in real_line.split(" -> "):
        rocks.append(tuple(map(int, t.split(','))))
    for i in range(len(rocks) - 1):
        r1 = rocks[i]
        r2 = rocks[i + 1]
        if r1[0] == r2[0]:
            for j in range(min(r1[1], r2[1]), max(r1[1], r2[1]) + 1):
                board[r1[0]][j] = ROCK
        else:
            for j in range(min(r1[0], r2[0]), max(r1[0], r2[0]) + 1):
                board[j][r1[1]] = ROCK

sands_fallen = 0
while True:
    new_sand = (500, 0)
    while new_sand[1] != HEIGHT:
        index = next((k for k, c in enumerate(board[new_sand[0]][new_sand[1]:], new_sand[1]) if c != AIR), HEIGHT) - 1
        if index + 1 == HEIGHT:
            print(f'Part 1 -> { sands_fallen }')
            sys.exit()
        if board[new_sand[0] - 1][index + 1] == AIR:
            new_sand = (new_sand[0] - 1, index + 1)
        elif board[new_sand[0] + 1][index + 1] == AIR:
            new_sand = (new_sand[0] + 1, index + 1)
        else:
            board[new_sand[0]][index] = SAND
            sands_fallen += 1
            break
