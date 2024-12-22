from util import *
from collections import *
import copy
from functools import reduce
from math import prod
import heapq

day = 16


def get_neighbors(tile, tiles):
    deltas = {"u": (0, -1), "r": (1, 0), "d": (0, 1), "l": (-1, 0)}
    dirs = ["u", "r", "d", "l"]
    x, y, dir = tile
    delta = deltas[dir]
    neighbors = set()
    if (x + delta[0], y + delta[1]) in tiles:
        neighbors.add((x + delta[0], y + delta[1], dir, 1))
    clockwise = dirs[(dirs.index(dir) + 1) % len(dirs)]
    counter_clockwise = dirs[(dirs.index(dir) - 1) % len(dirs)]
    neighbors.add((x, y, clockwise, 1000))
    neighbors.add((x, y, counter_clockwise, 1000))
    return neighbors


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    tiles = set()
    start = (-1, -1)
    end = (-1, -1)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#":
                continue
            p = (x, y)
            tiles.add(p)
            if c == "S":
                start = p
            elif c == "E":
                end = p

    dist = {}
    dirs = ["u", "r", "d", "l"]
    for tile in tiles:
        for dir in dirs:
            dist[(tile[0], tile[1], dir)] = 100000000

    start = (start[0], start[1], "r")
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while len(q) > 0:
        priority, u = heapq.heappop(q)
        for neighbor in get_neighbors(u, tiles):
            n_x, n_y, n_d, cost = neighbor
            d = dist[u] + cost
            if d < dist[(n_x, n_y, n_d)]:
                dist[(n_x, n_y, n_d)] = d
                heapq.heappush(q, (d, (n_x, n_y, n_d)))
    costs = [dist[(end[0], end[1], dir)] for dir in dirs]
    ans = min(costs)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    tiles = set()
    start = (-1, -1)
    end = (-1, -1)
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "#":
                continue
            p = (x, y)
            tiles.add(p)
            if c == "S":
                start = p
            elif c == "E":
                end = p

    dist = {}
    dirs = ["u", "r", "d", "l"]
    for tile in tiles:
        for dir in dirs:
            dist[(tile[0], tile[1], dir)] = 100000000

    start = (start[0], start[1], "r")
    dist[start] = 0
    q = []
    prev = defaultdict(set)
    heapq.heappush(q, (0, start))
    while len(q) > 0:
        priority, u = heapq.heappop(q)
        for neighbor in get_neighbors(u, tiles):
            n_x, n_y, n_d, cost = neighbor
            d = dist[u] + cost
            if d < dist[(n_x, n_y, n_d)]:
                dist[(n_x, n_y, n_d)] = d
                heapq.heappush(q, (d, (n_x, n_y, n_d)))
                prev[(n_x, n_y, n_d)] = {u}
            elif d == dist[(n_x, n_y, n_d)]:
                prev[(n_x, n_y, n_d)].add(u)

    end_costs = [(dist[p := (end[0], end[1], dir)], p) for dir in dirs]
    cheapest_ends = [e for e in end_costs if e[0] == min(end_costs)[0]]
    best_tiles = set()
    for cheapest_end in cheapest_ends:
        q = [cheapest_end[1]]
        while len(q) > 0:
            u = q.pop()
            best_tiles.add((u[0], u[1]))
            q.extend(prev[u])
    ans = len(best_tiles)
    print(ans)
    return ans


task1()
task2()
