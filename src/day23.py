from util import *
from collections import *
import copy
from functools import reduce
from math import prod
from itertools import combinations

day = 23


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    connections = defaultdict(set)
    for line in data:
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)

    combs = combinations(connections, 3)
    t_combs = [set(c) for c in combs if any(e.startswith("t") for e in c)]
    interconnections = []
    for i, comb in enumerate(t_combs):
        interconnected = True
        for element in comb:
            others = comb - {element}
            for other in others:
                if (
                    element not in connections[other]
                    or other not in connections[element]
                ):
                    interconnected = False
        if interconnected:
            interconnections.append(comb)
    ans = len(interconnections)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    connections = defaultdict(set)
    interconnected = set()
    for line in data:
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)
        interconnected.add(frozenset((a, b)))

    biggest_interconnection = set()
    while True:
        new_interconnections = set()
        for i, element in enumerate(connections):
            # if i % 10 == 0:
            # print(i, len(connections))
            for component in interconnected:
                if element in component:
                    continue
                connected = True
                for other in component:
                    if element not in connections[other]:
                        connected = False
                        break
                if connected:
                    new_interconnections.add(component.union({element}))
        # print(len(new_interconnections))
        if len(new_interconnections) == 1:
            biggest_interconnection = list(new_interconnections)[0]
            break
        interconnected = new_interconnections
    ans = ",".join(sorted(biggest_interconnection))
    print(ans)
    return ans


task1()
task2()
