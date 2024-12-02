from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 2


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    data = [[int(e) for e in line.split()] for line in data]
    ans = 0
    for line in data:
        deltas = []
        for i in range(1, len(line)):
            e1 = line[i - 1]
            e2 = line[i]
            d = e2 - e1
            deltas.append(d)
        if set(deltas) - {1,2,3} == set():
            ans += 1
        if set(deltas) - {-1,-2,-3} == set():
            ans += 1
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")
    data = [[int(e) for e in line.split()] for line in data]
    ans = 0
    for line in data:
        potential_deltas = []
        for i in range(len(line)):
            new_line = line[:i] + line[i + 1:]
            deltas = []
            for j in range(1, len(new_line)):
                e1 = new_line[j - 1]
                e2 = new_line[j]
                d = e2 - e1
                deltas.append(d)
            potential_deltas.append(deltas)

        for delta in potential_deltas:
            if set(delta) - {1,2,3} == set() or set(delta) - {-1,-2,-3} == set():
                ans += 1
                break
    print(ans)
    return ans

task1()
task2()
