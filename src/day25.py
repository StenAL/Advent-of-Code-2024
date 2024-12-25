from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 25


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    keys = []
    locks = []
    height = -1
    for group in data:
        l = len(group[0])
        data_type = "lock" if group[0] == l * "#" else "key"
        cols = defaultdict(int)
        for y, line in enumerate(group):
            height = max(y + 1, height)
            for x, c in enumerate(line):
                v = 1 if c == "#" else 0
                cols[x] += v
        heights = [v for k, v in sorted(cols.items())]
        if data_type == "lock":
            locks.append(heights)
        else:
            keys.append(heights)
    valid_combinations = 0
    for lock in locks:
        for key in keys:
            valid = True
            for i in range(len(key)):
                if lock[i] + key[i] > height:
                    valid = False
                    break
            if valid:
                valid_combinations += 1
    ans = valid_combinations
    print(ans)
    return ans


task1()
