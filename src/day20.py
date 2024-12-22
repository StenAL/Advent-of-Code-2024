from util import *
from collections import *
import copy
from functools import reduce, cache
from math import prod
import heapq

day = 20


def get_neighbors(tile, tiles):
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y = tile
    neighbors = tuple(
        n for delta in deltas if (n := (x + delta[0], y + delta[1])) in tiles
    )
    return neighbors


def get_cheats(tile, tiles):
    deltas = [(0, -2), (2, 0), (0, 2), (-2, 0)]
    x, y = tile
    cheats = tuple(
        n for delta in deltas if (n := (x + delta[0], y + delta[1])) in tiles
    )
    return cheats


def djikstra(start, neighbors, edges):
    dist = {}
    for tile in neighbors:
        dist[tile] = 100000000

    start = (start[0], start[1])
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while len(q) > 0:
        priority, u = heapq.heappop(q)
        for neighbor in neighbors[u]:
            n = neighbor
            d = dist[u] + edges[u, n]
            if d < dist[n]:
                dist[n] = d
                heapq.heappush(q, (d, n))
    return dist


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

    neighbors = {}
    edges = {}
    for tile in tiles:
        ns = get_neighbors(tile, tiles)
        neighbors[tile] = ns
        for n in ns:
            edges[tile, n] = 1
            edges[n, tile] = 1

    dist_from_end = djikstra(end, neighbors, edges)
    dist_from_start = djikstra(start, neighbors, edges)
    regular_time = dist_from_start[end]

    cheat_times = []
    for tile in tiles:
        cheats = get_cheats(tile, tiles)
        for cheat in cheats:
            time_to_tile = dist_from_start[tile]
            time_to_cheat = abs(cheat[0] - tile[0]) + abs(cheat[1] - tile[1])
            time_to_end = dist_from_end[cheat]
            total_time = time_to_tile + time_to_cheat + time_to_end
            cheat_times.append(total_time)
    savings = Counter(regular_time - time for time in cheat_times)
    ans = sum(v for k, v in savings.items() if k >= 100)
    print(ans)
    return ans


@cache
def get_deltas():
    deltas = set()
    for d1 in range(21):
        for d2 in range(21 - d1):
            deltas.update([(d1, d2), (d1, -d2), (-d1, d2), (-d1, -d2)])
    return deltas


def get_cheats2(tile, tiles):
    deltas = get_deltas()
    x, y = tile
    cheats = tuple(
        n for delta in deltas if (n := (x + delta[0], y + delta[1])) in tiles
    )
    return cheats


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

    neighbors = {}
    edges = {}
    for tile in tiles:
        ns = get_neighbors(tile, tiles)
        neighbors[tile] = ns
        for n in ns:
            edges[tile, n] = 1
            edges[n, tile] = 1

    dist_from_end = djikstra(end, neighbors, edges)
    dist_from_start = djikstra(start, neighbors, edges)
    regular_time = dist_from_start[end]

    cheat_times = []
    for tile in sorted(tiles):
        cheats = get_cheats2(tile, tiles)
        for cheat in cheats:
            time_to_tile = dist_from_start[tile]
            time_to_cheat = abs(cheat[0] - tile[0]) + abs(cheat[1] - tile[1])
            time_to_end = dist_from_end[cheat]
            total_time = time_to_tile + time_to_cheat + time_to_end
            cheat_times.append(total_time)
    savings = Counter(regular_time - time for time in cheat_times)
    ans = sum(v for k, v in savings.items() if k >= 100)
    print(ans)
    return ans


task1()
task2()
