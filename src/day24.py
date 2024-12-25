from util import *
from collections import *
import copy
from functools import reduce
from math import prod
from itertools import combinations
import re

day = 24


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test2")
    states_data, rules_data = data
    states = dict(line.split(": ") for line in states_data)
    states = {k: True if v == "1" else False for k, v in states.items()}
    all_wires = set(states.keys())
    rules = []
    for line in rules_data:
        left, right = line.split(" -> ")
        a, op, b = left.split(" ")
        rules.append((a, op, b, right))
        all_wires.update({a, b, right})

    z_wires = {w for w in all_wires if w.startswith("z")}
    while True:
        new_states = states.copy()
        for rule in rules:
            a, op, b, dest = rule
            if a not in states or b not in states:
                continue
            a = states[a]
            b = states[b]
            if op == "AND":
                new_states[dest] = a and b
            elif op == "OR":
                new_states[dest] = a or b
            elif op == "XOR":
                new_states[dest] = a ^ b
        states = new_states
        if all(z_wire in states for z_wire in z_wires):
            break
    bits = ["1" if states[wire] else "0" for wire in sorted(z_wires, reverse=True)]
    bits = "".join(bits)
    ans = int(bits, 2)
    print(ans)


def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test2")
    states_data, rules_data = data
    rules = {}
    for line in rules_data:
        left, right = line.split(" -> ")
        a, op, b = left.split(" ")
        left = f" {op} ".join(sorted((a, b)))
        rules[right] = left

    tmp = rules["z07"]
    rules["z07"] = rules["gmt"]
    rules["gmt"] = tmp
    tmp = rules["z18"]
    rules["z18"] = rules["dmn"]
    rules["dmn"] = tmp
    tmp = rules["qjj"]
    rules["qjj"] = rules["cbj"]
    rules["cbj"] = tmp
    tmp = rules["cfk"]
    rules["cfk"] = rules["z35"]
    rules["z35"] = tmp
    for wire, rule in sorted(rules.items()):
        if not wire.startswith("z"):
            continue
        s = []
        for token in rule.split(" "):
            if token in rules:
                s.append(rules[token])
            else:
                s.append(token)
        s = f" {s[1]} ".join(sorted((s[0], s[2])))
        # print(f"{wire}: {s}")
        if wire in ["z00", "z01", "z45"]:  # special case for first and last wires
            continue
        if not re.search(
            "\\w+ OR \\w+ XOR \\w+ XOR \\w+", s
        ):  # ghp OR qfs XOR x32 XOR y32
            print(f"{wire} is invalid!")

    changed = ["z07", "gmt", "z18", "dmn", "qjj", "cbj", "cfk", "z35"]
    ans = ",".join(sorted(changed))
    print(ans)


task1()
task2()
