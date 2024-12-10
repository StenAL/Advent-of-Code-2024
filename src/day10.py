from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 10


def get_neighbors(p, points):
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y, v = p
    neighbors = {(x + dx, y + dy, v + 1) for dx, dy in deltas if (x + dx, y + dy) in points and points[(x + dx, y + dy)] == v + 1}
    return neighbors
    

def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    points = {}
    starts = set()
    for y, line in enumerate(data):
        for x, n in enumerate(line):
            if n == "0":
                starts.add((x, y, 0))
            else:
                points[(x, y)] = int(n)
    
    ans = 0
    for start in starts:
        reachable_tops = 0
        current = {start}
        while True:
            new = set()
            for p in current:
                new.update(get_neighbors(p, points))
            if len(new) == 0:
                break
            current = new
        reachable_tops = len([p for p in current if p[2] == 9])
        ans += reachable_tops
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    points = {}
    starts = set()
    for y, line in enumerate(data):
        for x, n in enumerate(line):
            if n == "0":
                starts.add((x, y, 0))
            else:
                points[(x, y)] = int(n)
    
    ans = 0
    for start in starts:
        ratings = defaultdict(int)
        reachable_tops = 0
        current = {start}
        ratings[(start[0], start[1])] = 1

        while len(current) > 0:
            new = set()
            for p in current:
                rating = ratings[(p[0], p[1])]
                neighbors = get_neighbors(p, points)
                for n in neighbors:
                    ratings[(n[0], n[1])] += rating
                new.update(neighbors)
            if len(new) == 0:
                break
            current = new
        reachable_tops = sum(ratings[(p[0], p[1])] for p in current if p[2] == 9)
        ans += reachable_tops
    print(ans)
    return ans

task1()
task2()
