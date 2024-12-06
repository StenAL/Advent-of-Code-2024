from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 6


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    l = len(data)
    obstacles = set()
    position = (0, 0)
    for y in range(l):
        for x in range(len(data[y])):
            c = data[y][x]
            if c == "#":
                obstacles.add((x, y)) 
            elif c == "^":
                position = (x, y)

    seen = set()
    deltas = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
    turns = {"up": "right", "right": "down", "down": "left", "left": "up"}
    dir = "up"

    while True:
        x, y = position
        if x == -1 or x == l or y == -1 or y == l:
            break
        seen.add(position)
        d = deltas[dir]
        new_position = (x + d[0], y + d[1])
        if new_position in obstacles:
            dir = turns[dir]
        else:
            position = new_position

    ans = len(seen)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    l = len(data)
    obstacles = set()
    initial_position = (0, 0)
    for y in range(l):
        for x in range(len(data[y])):
            c = data[y][x]
            if c == "#":
                obstacles.add((x, y)) 
            elif c == "^":
                initial_position = (x, y)

    deltas = {"up": (0, -1), "right": (1, 0), "down": (0, 1), "left": (-1, 0)}
    turns = {"up": "right", "right": "down", "down": "left", "left": "up"}
    loops = 0

    for y_obstacle in range(l):
        for x_obstacle in range(len(data[y_obstacle])):
            if ((x_obstacle, y_obstacle) == initial_position):
                continue
            new_obstacles = obstacles.union({(x_obstacle, y_obstacle)})
            position = initial_position
            seen = set()
            dir = "up"

            while True:
                x, y = position
                if (position, dir) in seen:
                    loops += 1
                    break
                if x == -1 or x == l or y == -1 or y == l:
                    break
                seen.add((position, dir))
                d = deltas[dir]
                new_position = (x + d[0], y + d[1])
                if new_position in new_obstacles:
                    dir = turns[dir]
                else:
                    position = new_position
    ans = loops
    print(ans)
    return ans


task1()
task2()
