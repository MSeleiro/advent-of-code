from functools import cmp_to_key

pairs = []

for line in open("./input.txt").readlines():
    if line != "\n":
        pairs.append(eval(line.strip("\n")))


def correct(left, right) -> tuple[bool, bool]:
    if type(left) == int and type(right) == int:
        return left == right, left < right
    elif type(left) == list and type(right) == int:
        return correct(left, [right])
    elif type(left) == int and type(right) == list:
        return correct([left], right)
    else:
        ret = (len(left) == len(right), len(left) < len(right))
        length = len(left) if ret[1] else len(right)
        for idx in range(length):
            res = correct(left[idx], right[idx])
            if not res[0]:
                ret = res
                break
        return ret


correct_pairs = []

current_pair = 1
for i in range(len(pairs)):
    if i % 2 == 0:
        if correct(pairs[i], pairs[i + 1])[1]:
            correct_pairs.append(current_pair)
        current_pair += 1

print(f'Part 1 -> { sum(correct_pairs) }')

dist1 = eval('[[2]]')
dist2 = eval('[[6]]')

pairs.append(dist1)
pairs.append(dist2)

pairs.sort(key=cmp_to_key(lambda item1, item2: -1 if correct(item1, item2)[1] else 1))

print(f'Part 2 -> {(pairs.index(dist1) + 1) * (pairs.index(dist2) + 1) }')
