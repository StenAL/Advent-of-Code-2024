from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 7

def get_sums(acc, components):
    if len(components) == 0:
        return {acc}
    next = components[0]
    rest = components[1:]
    added = get_sums(acc + next, rest)
    mult = get_sums(acc * next, rest)
    return added.union(mult)



def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ans = 0
    for line in data:
        target, components = line.split(": ")
        target = int(target)
        components = [int(e) for e in components.split(" ")]
        sums = get_sums(0, components)
        if target in sums:
            ans += target
    print(ans)
    return ans


def get_sums2(acc, components, target, memo):
    if len(components) == 0:
        return {acc}
    if acc > target:
        return set()
    if (acc, components) in memo:
        return memo[(acc, components)]
    next = components[0]
    rest = components[1:]
    added = get_sums2(acc + next, rest, target, memo)
    mult = get_sums2(max(acc, 1) * next, rest, target, memo)
    concat = get_sums2(int(str(acc) + str(next)), rest, target, memo)
    # all = added.union(mult)
    all = added.union(mult, concat)
    memo[(acc, components)] = all
    return all


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ans = 0
    for line in data:
        target, components = line.split(": ")
        target = int(target)
        components = tuple(int(e) for e in components.split(" "))
        sums = get_sums2(0, components, target, {})
        if target in sums:
            print("T: " + line)
            ans += target
        else:
            print("F: " + line)
    print(ans)
    return ans

# task1()
task2() # 348360612577977 too low
        # 348360680517522 too high
        # 348360680517522 ?
