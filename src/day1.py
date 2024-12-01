from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 1


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    pairs = [line.split() for line in data]
    pairs = [(int(pair[0]), int(pair[1])) for pair in pairs]
    l1 = [p[0] for p in pairs]
    l2 = [p[1] for p in pairs]
    ans = 0
    for e1, e2 in zip(sorted(l1), sorted(l2)):
        ans += abs(e1 - e2)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    pairs = [line.split() for line in data]
    pairs = [(int(pair[0]), int(pair[1])) for pair in pairs]
    l1 = [p[0] for p in pairs]
    l2 = [p[1] for p in pairs]
    counts = Counter(l2)
    ans = sum(counts[e] * e for e in l1)
    print(ans)
    return ans


task1()
task2()
