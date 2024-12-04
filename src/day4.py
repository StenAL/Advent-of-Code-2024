from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 4


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    # data = get_input_for_file("test2")

    l = len(data)
    rotated = ["".join([data[l - 1 - y][x] for y in range(len(data))]) for x in range(len(data[0]))]

    diagonals = []
    first_iteration = True
    for x in range(len(data[0])):
        y = 0
        diagonal = []
        diagonal2 = []
        diagonal3 = []
        diagonal4 = []
        while y < len(data) and x < len(data):
            diagonal.append(data[y][x])
            diagonal2.append(data[x][y])
            diagonal3.append(rotated[y][x])
            diagonal4.append(rotated[x][y])
            x += 1
            y += 1
        diagonal_string = "".join(diagonal)
        diagonal_string2 = "".join(diagonal2)
        diagonal_string3 = "".join(diagonal3)
        diagonal_string4 = "".join(diagonal4)
        diagonals.append(diagonal_string)
        diagonals.append(diagonal_string3)
        if not first_iteration:
            diagonals.append(diagonal_string2)
            diagonals.append(diagonal_string4)
        first_iteration = False

    ans = 0
    lines = data + rotated + diagonals
    for line in lines:
        ans += line.count("XMAS")
        ans += line[::-1].count("XMAS")
    print(ans)
    return ans



def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    # data = get_input_for_file("test2")

    l = len(data)
    ans = 0
    for y in range(l):
        for x in range(l):
            if x == 0 or x == l - 1 or y == 0 or y == l - 1:
                continue
            diag1 = data[y-1][x-1] + data[y][x] + data[y+1][x+1]
            diag2 = data[y-1][x+1] + data[y][x] + data[y+1][x-1]
            targets = ["MAS", "SAM"]
            if diag1 in targets and diag2 in targets:
                ans += 1
    print(ans)
    return ans



task1()
task2()
