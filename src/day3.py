from util import *
from collections import *
import copy
from functools import reduce
from math import prod
import re

day = 3


def task1():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")

    ans = 0
    for line in data:
        matches = re.findall(r'mul\(\d+,\d+\)', line)
        for match in matches:
            e1, e2 = match.strip("mul(").rstrip(")").split(",")
            ans += int(e1) * int(e2)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    #data = get_input_for_file("test")

    ans = 0
    enabled = True

    for line in data:
        matches = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', line)
        for match in matches:
            if match == "do()":
                enabled = True
                continue
            if match == "don't()":
                enabled = False
                continue
            e1, e2 = match.strip("mul(").rstrip(")").split(",")
            if enabled:
                ans += int(e1) * int(e2)
    print(ans)
    return ans


task1()
task2()
