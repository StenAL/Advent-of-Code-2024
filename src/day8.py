from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 8


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    antennas = defaultdict(set)
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = data[y][x]
            if c != ".":
                antennas[c].add((x, y))
    antinodes = set()
    for signal, locations in antennas.items():
        for l1 in locations:
            x1, y1 = l1
            for l2 in locations:
                x2, y2 = l2
                if l1 == l2:
                    continue
                dy = y2 - y1
                dx = x2 - x1
                p1 = x1 + 2 * dx, y1 + 2 * dy
                p2 = x1 - dx, y1 - dy
                antinodes.add(p1)
                antinodes.add(p2)
    antinodes = {p for p in antinodes if 0 <= p[0] < len(data) and 0 <= p[1] < len(data)}
    ans = len(antinodes)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    antennas = defaultdict(set)
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = data[y][x]
            if c != ".":
                antennas[c].add((x, y))
    antennas = {k: v for k, v in antennas.items() if len(v) > 1}
    antinodes = set().union(*antennas.values())
    for signal, locations in antennas.items():
        for l1 in locations:
            x1, y1 = l1
            for l2 in locations:
                x2, y2 = l2
                if l1 == l2:
                    continue
                dy = y2 - y1
                dx = x2 - x1
                x = x1
                y = y1
                while 0 <= x < len(data) and 0 <= y < len(data):
                    antinodes.add((x, y))
                    x = x - dx
                    y = y - dy
                x = x1
                y = y1
                while 0 <= x < len(data) and 0 <= y < len(data):
                    antinodes.add((x, y))
                    x = x + dx
                    y = y + dy

    ans = len(antinodes)
    print(ans)
    return ans


task1()
task2()
