from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 14


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    robots = []
    len_x = 101
    len_y = 103
    # len_x = 11
    # len_y = 7
    for line in data:
        p, v = line.split(" v=")
        p = tuple(int(e) for e in p.strip("p=").split(","))
        v = tuple(int(e) for e in v.split(","))
        robot = {"position": p, "velocity": v}
        robots.append(robot)
    time = 100
    positions = []
    for robot in robots:
        p = robot["position"]
        v = robot["velocity"]
        new_x = (p[0] + v[0] * time) % len_x
        new_y = (p[1] + v[1] * time) % len_y
        positions.append((new_x, new_y))
    ans = 0
    quad_robots = defaultdict(int)
    for position in positions:
        y_mid = (len_y - 1) / 2
        x_mid = (len_x - 1) / 2
        if position[0] < x_mid and position[1] < y_mid:
            quad_robots[0] += 1
        elif position[0] > x_mid and position[1] < y_mid:
            quad_robots[1] += 1
        elif position[0] < x_mid and position[1] > y_mid:
            quad_robots[2] += 1
        elif position[0] > x_mid and position[1] > y_mid:
            quad_robots[3] += 1
    ans = prod(quad_robots.values())
    print(ans)


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    robots = {}
    len_x = 101
    len_y = 103
    # len_x = 11
    # len_y = 7
    for line in data:
        p, v = line.split(" v=")
        p = tuple(int(e) for e in p.strip("p=").split(","))
        v = tuple(int(e) for e in v.split(","))
        robots[v] = p
    time = 0
    print_result = False
    while True:
        time += 1
        positions = set()
        position_by_x = defaultdict(set)
        position_by_y = defaultdict(set)
        for v, p in robots.items():
            new_x = (p[0] + v[0] * time) % len_x
            new_y = (p[1] + v[1] * time) % len_y
            positions.add((new_x, new_y))
            position_by_x[new_x].add(new_y)
            position_by_y[new_y].add(new_x)

        long_x_rows = 0
        long_y_rows = 0
        for x, y_values in position_by_x.items():
            if len(y_values) > 11:
                long_x_rows += 1
        for y, x_values in position_by_y.items():
            if len(x_values) > 11:
                long_y_rows += 1
        if long_x_rows > 6 and long_y_rows > 1:
            if print_result:
                for y in range(len_y):
                    for x in range(len_x):
                        if y in position_by_x[x]:
                            print("#", end="")
                        else:
                            print(".", end="")
                    print()
            break
    ans = time
    print(ans)
    return ans


task1()
task2()
