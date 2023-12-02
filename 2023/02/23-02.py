#
#   --- Day 2: Cube Conundrum ---
#

import re
from functools import reduce

def part1(lines: list[str]) -> int:
    limit = {"red" : 12, "green" : 13, "blue" : 14}
    sum = 0
    for id, game in enumerate(lines):
        valid = True
        for set in game.split(":")[1].split(";"):
            blue = re.findall(r"\d+ blue", set)
            red = re.findall(r"\d+ red", set)
            green = re.findall(r"\d+ green", set)
            for val in [blue, red, green]:
                if len(val):
                    splt = val[0].split(" ")
                    if int(splt[0]) > limit[splt[1]]:
                        valid = False

        if valid:
            sum += (id + 1)
            
    return sum

def part2(lines: list[str]) -> int:
    idx = {"red" : 0, "green" : 1, "blue" : 2}
    sum = 0
    for game in lines:
        maxs = [0, 0, 0]
        for set in game.split(":")[1].split(";"):
            blue = re.findall(r"\d+ blue", set)
            red = re.findall(r"\d+ red", set)
            green = re.findall(r"\d+ green", set)
            for val in [blue, red, green]:
                if len(val):
                    splt = val[0].split(" ")
                    color = splt[1]
                    maxs[idx[color]] = max(int(splt[0]), maxs[idx[color]])
        
        sum += reduce(lambda x, y: x * y, maxs)
    
    return sum

with open("input.txt", "r") as f:
    lines = f.readlines()
    print(part1(lines))
    print(part2(lines))