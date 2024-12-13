from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 12

def get_neighbors(p, grid):
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    points = map(lambda d: (p[0] + d[0], p[1] + d[1]), deltas)
    return {point for point in points if grid[p] == grid[point]}

def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    grid = defaultdict(str)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x,y)] = c
    regions = []
    seen = set()
    points = [p for p in grid.keys()]
    for p in points:
        if p in seen:
            continue
        q = deque([p])
        region = {p}
        while len(q) > 0:
            p = q.pop()
            seen.add(p)
            neighbors = get_neighbors(p, grid)
            region.update(neighbors)
            q.extend(n for n in neighbors if n not in seen)
        regions.append(region)


    ans = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for p in region:
            perimeter += 4 - len(get_neighbors(p, grid))
        cost = area * perimeter
        ans += cost
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")

    grid = defaultdict(str)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x,y)] = c
    regions = []
    seen = set()
    points = [p for p in grid.keys()]
    for p in points:
        if p in seen:
            continue
        q = deque([p])
        region = {p}
        while len(q) > 0:
            p = q.pop()
            seen.add(p)
            neighbors = get_neighbors(p, grid)
            region.update(neighbors)
            q.extend(n for n in neighbors if n not in seen)
        regions.append(region)


    ans = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        rights = defaultdict(list)
        lefts = defaultdict(list)
        ups = defaultdict(list)
        downs = defaultdict(list)
        for p in region:
            if (right := (p[0] + 1, p[1])) not in get_neighbors(p, grid):
               rights[right[0]].append(right[1]) 
            if (left := (p[0] - 1, p[1])) not in get_neighbors(p, grid):
               lefts[left[0]].append(left[1]) 
            if (up := (p[0], p[1] - 1)) not in get_neighbors(p, grid):
               ups[up[1]].append(up[0]) 
            if (down := (p[0], p[1] + 1)) not in get_neighbors(p, grid):
               downs[down[1]].append(down[0]) 
        # print("right", rights)
        # print("left", lefts)
        # print("up", ups)
        # print("down", downs)
        perimeter = list(ups.values()) + list(downs.values()) + list(lefts.values()) + list(rights.values())
        edges = len(perimeter)
        for v in perimeter:
            v = sorted(v)
            for i in range(1, len(v)):
                if v[i] - v[i - 1] > 1:
                    edges += 1
        cost = area * edges
        ans += cost
    print(ans)
    return ans

task1()
task2()
