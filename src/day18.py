from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 18

def get_neighbors(p, x_max, y_max, corrupted):
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    neighbors = [n for d in deltas if (n := (p[0] + d[0], p[1] + d[1])) not in corrupted]
    neighbors = [n for n in neighbors if 0 <= n[0] <= x_max and 0 <= n[1] <= y_max]
    return neighbors

def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    falling = [tuple(int(e) for e in l.split(",")) for l in data]
    seconds = 1024
    corrupted = set(falling[:seconds])
    start = (0, 0)
    current = {start}
    steps = 0
    x_max = 70
    y_max = 70
    end = (x_max, y_max)
    while end not in current:
        new_current = set()
        for p in current:
            new_current.update(get_neighbors(p, x_max, y_max, corrupted))
        current = new_current
        steps += 1
    ans = steps
    print(ans)
    return ans




def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    falling = [tuple(int(e) for e in l.split(",")) for l in data]
    start = (0, 0)
    x_max = 70
    y_max = 70
    end = (x_max, y_max)
    seconds = 0
    while True:
        corrupted = set(falling[:seconds])
        seen = set()
        q = [start]
        while len(q) > 0:
            p = q.pop()
            if p in seen:
                continue
            seen.add(p)
            q.extend(get_neighbors(p, x_max, y_max, corrupted))
        if end in seen:
            # print(seconds)
            pass
        else:
            break
        seconds += 1
    blocker = falling[seconds - 1]
    ans = ",".join(map(str, blocker))
    print(ans)
    return ans


task1()
task2()
