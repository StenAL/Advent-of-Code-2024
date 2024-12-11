from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 11


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0]
    stones = [int(e) for e in data.split()]
    steps = 25
    for i in range(steps):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
                continue
            str_stone = str(stone)
            str_len = len(str_stone)
            if str_len % 2 == 0:
                new_stones.append(int(str_stone[:str_len // 2]))
                new_stones.append(int(str_stone[str_len // 2:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    ans = len(stones)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0]
    stones = Counter([int(e) for e in data.split()])
    steps = 75
    for i in range(steps):
        new_stones = defaultdict(int)
        for stone, v in stones.items():
            if stone == 0:
                new_stones[1] += v
                continue
            str_stone = str(stone)
            str_len = len(str_stone)
            if str_len % 2 == 0:
                new_stones[(int(str_stone[:str_len // 2]))] += v
                new_stones[(int(str_stone[str_len // 2:]))] += v
            else:
                new_stones[stone * 2024] += v
        stones = new_stones
    ans = sum(v for v in stones.values())
    print(ans)
    return ans


task1()
task2()
