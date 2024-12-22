from util import *
from collections import *
import copy
from functools import reduce, cache
from math import prod

day = 19


@cache
def construct(pattern, carpets):
    if len(pattern) == 0:
        return True
    attempts = []
    for carpet in carpets:
        if pattern.startswith(carpet):
            attempts.append(construct(pattern.removeprefix(carpet), carpets))
    return any(attempts)


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    carpets, patterns = data
    carpets = tuple(carpets[0].split(", "))
    possible_count = 0
    for pattern in patterns:
        possible = construct(pattern, carpets)
        possible_count += 1 if possible else 0
    ans = possible_count
    print(ans)
    return ans


@cache
def construct2(pattern, carpets):
    if len(pattern) == 0:
        return 1
    attempts = []
    for carpet in carpets:
        if pattern.startswith(carpet):
            attempts.append(construct2(pattern.removeprefix(carpet), carpets))
    return sum(attempts)


def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    carpets, patterns = data
    carpets = tuple(carpets[0].split(", "))
    possible_count = 0
    for pattern in patterns:
        paths = construct2(pattern, carpets)
        possible_count += paths
    ans = possible_count
    print(ans)
    return ans


task1()
task2()
