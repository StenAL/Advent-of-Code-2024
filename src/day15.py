from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 15


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    grid, instructions = data
    robot = (-1, -1)
    boxes = set()
    walls = set()
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "@":
                robot = (x, y)
            elif c == "O":
                boxes.add((x, y))
            elif c == "#":
                walls.add((x, y))
    instructions = "".join(instructions)
    instruction_to_d = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
    for instruction in instructions:
        x, y = robot
        d = instruction_to_d[instruction]
        moved_boxes = set()
        should_move = False
        current = robot
        while True:
            current = current[0] + d[0], current[1] + d[1]
            if current in walls:
                break
            elif current in boxes:
                moved_boxes.add(current)
            else:  # free space
                should_move = True
                break
        if should_move:
            boxes.difference_update(moved_boxes)
            boxes.update([(b[0] + d[0], b[1] + d[1]) for b in moved_boxes])
            robot = (x + d[0], y + d[1])
            # print(instruction, "move to", robot)
        # else:
        # print(instruction, "stay")
    coords = [b[0] + b[1] * 100 for b in boxes]
    ans = sum(coords)
    print(ans)
    return ans


def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    grid, instructions = data
    grid = [
        l.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
        for l in grid
    ]
    robot = (-1, -1)
    boxes = set()
    box_to_squares = defaultdict(set)
    walls = set()
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "@":
                robot = (x, y)
            elif c == "[":
                boxes.add((x, y))
                boxes.add((x + 1, y))
                squares = {(x, y), (x + 1, y)}
                box_to_squares[(x, y)] = squares
                box_to_squares[(x + 1, y)] = squares
            elif c == "#":
                walls.add((x, y))
    instructions = "".join(instructions)
    instruction_to_d = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}

    for instruction in instructions:
        d = instruction_to_d[instruction]
        moved_boxes = set()
        should_move = True
        q = [robot]
        seen = set()
        while len(q) > 0:
            current = q.pop()
            current = current[0] + d[0], current[1] + d[1]
            if current in seen:
                continue
            seen.add(current)
            if current in walls:
                should_move = False
                break
            elif current in boxes:
                squares = box_to_squares[current]
                moved_boxes.update(squares)
                q.extend(squares)
            else:  # free space
                continue
        if should_move:
            removed = set()
            added = set()
            new_box_to_squares = {}
            for box in moved_boxes:
                squares = box_to_squares[box]
                removed.update(squares)
                new_squares = {(b[0] + d[0], b[1] + d[1]) for b in squares}
                added.update(new_squares)
                for new_square in new_squares:
                    new_box_to_squares[new_square] = new_squares

            for b in removed:
                boxes.remove(b)
                del box_to_squares[b]
            for b in added:
                boxes.add(b)
                box_to_squares[b] = new_box_to_squares[b]
            robot = (robot[0] + d[0], robot[1] + d[1])
            # print(instruction, "move to", robot)
            # print(f">> remove {removed}, add {added}")
        # else:
        # print(instruction, "stay")
    ans = 0
    top_lefts = set()
    for squares in box_to_squares.values():
        top_left = sorted(squares)[0]
        top_lefts.add(top_left)
    ans = sum(b[0] + b[1] * 100 for b in top_lefts)
    print(ans)
    return ans


# task1()
task2()
