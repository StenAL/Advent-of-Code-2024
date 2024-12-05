from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 5


def task1():
    data = get_grouped_input_for_day(day)
    #data = get_grouped_input_for_file("test")
    rules, manuals = data
    needs = defaultdict(set)
    needed_by = defaultdict(set)
    for line in rules:
        before, after = [int(e) for e in line.split("|")]
        needs[after].add(before)
        needed_by[before].add(after)

    valid_manuals = []
    for line in manuals:
        pages = [int(e) for e in line.split(",")]
        valid = True
        seen = set()
        for page in pages:
            # print(page, needs[page].intersection(pages), valid)
            if len(needs[page].intersection(pages) - seen) > 0:
                valid = False
            seen.add(page)
        if valid:
            valid_manuals.append(pages)

    ans = 0
    ans += sum(l[len(l) // 2] for l in valid_manuals)
    print(ans)
    return ans



def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    rules, manuals = data
    needs = defaultdict(set)
    needed_by = defaultdict(set)
    for line in rules:
        before, after = [int(e) for e in line.split("|")]
        needs[after].add(before)
        needed_by[before].add(after)

    invalid_manuals = []
    for line in manuals:
        pages = [int(e) for e in line.split(",")]
        valid = True
        seen = set()
        for page in pages:
            if len(needs[page].intersection(pages) - seen) > 0:
                valid = False
            seen.add(page)
        if not valid:
            invalid_manuals.append(pages)

    valid_manuals = []
    for line in invalid_manuals:
        valid = []
        while len(valid) != len(line):
            for el in line:
                before = needs[el].intersection(line) - set(valid)
                if len(before) == 0 and el not in valid:
                    valid.append(el)
        valid_manuals.append(valid)

    ans = 0
    ans += sum(l[len(l) // 2] for l in valid_manuals)
    print(ans)
    return ans

task1()
task2()
