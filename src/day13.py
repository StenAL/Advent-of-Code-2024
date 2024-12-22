from util import *
from collections import *
import copy
from functools import reduce, cache
from math import prod

day = 13


@cache
def get_tokens(a, b, target, presses=(0, 0)):
    if target[0] == 0 and target[1] == 0:
        return 0
    if target[0] < 0 or target[1] < 0:
        return None
    if presses[0] > 100 or presses[1] > 100:
        return None
    a_pressed = target[0] - a[0], target[1] - a[1]
    a_tokens = get_tokens(a, b, a_pressed, (presses[0] + 1, presses[1]))
    b_pressed = target[0] - b[0], target[1] - b[1]
    b_tokens = get_tokens(a, b, b_pressed, (presses[0], presses[1] + 1))
    if a_tokens is None and b_tokens is None:
        return None
    if a_tokens is None:
        return 1 + b_tokens
    if b_tokens is None:
        return 3 + a_tokens
    return min(3 + a_tokens, 1 + b_tokens)


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")

    ans = 0
    for group in data:
        a, b, target = group
        a = tuple(int(e) for e in a.split(": X+")[1].split(", Y+"))
        b = tuple(int(e) for e in b.split(": X+")[1].split(", Y+"))
        target = tuple(int(e) for e in target.split(": X=")[1].split(", Y="))
        tokens = get_tokens(a, b, target)
        if tokens is not None:
            ans += tokens
    print(ans)
    return ans


def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")

    ans = 0
    offset = 10000000000000
    for group in data:
        a, b, target = group
        a_x, a_y = tuple(int(e) for e in a.split(": X+")[1].split(", Y+"))
        b_x, b_y = tuple(int(e) for e in b.split(": X+")[1].split(", Y+"))
        target_x, target_y = tuple(
            int(e) + offset for e in target.split(": X=")[1].split(", Y=")
        )
        # a_x*a + b_x * b = target_x  ==> a = (target_x - b_x * b) / a_x
        # a_y*a + b_y * b = target_y  ==> a = (target_y - b_y * b) / a_y
        #
        # (target_x - b_x * b) / a_x = (target_y - b_y * b) / a_y
        # a_y * target_x - b_x * b * a_y = a_x * target_y - b_y * b * a_x
        # b_y * b * a_x - b_x * b * a_y = a_x * target_y - a_y * target_x
        # b = (a_x * target_y - a_y * target_x) / (b_y * a_x - b_x * a_y)
        b = (a_x * target_y - a_y * target_x) / (b_y * a_x - b_x * a_y)
        a = (target_y - b_y * b) / a_y
        if int(a) != a or int(b) != b:
            continue

        tokens = 3 * a + b
        ans += int(tokens)

    print(ans)
    return ans


task1()
task2()
