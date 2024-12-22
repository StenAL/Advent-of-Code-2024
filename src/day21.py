from util import *
from collections import *
import copy
from functools import reduce, cache
from math import prod
from collections.abc import Sequence, Collection

day = 21


def get_neighbors_grid(tile: tuple[int, int], tiles: Collection[tuple[int, int]]):
    deltas = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    x, y = tile
    neighbors = {
        k: n for k, v in deltas.items() if (n := (x + v[0], y + v[1])) in tiles
    }
    return neighbors


def get_neighbors(
    state: tuple[str, ...], arrows_grid_neighbors, numbers_grid_neighbors, memo
):
    if state in memo:
        return memo[state]
    neighbors = set()
    # can press any button on first grid to move second grid
    for dir in arrows_grid_neighbors.keys():
        if dir == "A":
            continue
        if dir in arrows_grid_neighbors[state[0]]:
            new_element = arrows_grid_neighbors[state[0]][dir]
            neighbors.add((new_element,) + state[1:])

    # if first N grids are A, can press A on first grid to activate grid to move on grid N + 1
    non_a = [i for i, s in enumerate(state) if s != "A"]
    if len(non_a) > 0 and non_a[0] != len(state) - 1:
        i = non_a[0]
        new_element = state[i + 1]
        if i != len(state) - 2:
            # arrow grid
            if state[i] in arrows_grid_neighbors[state[i + 1]]:
                new_element = arrows_grid_neighbors[state[i + 1]][state[i]]
        else:
            if state[i] in numbers_grid_neighbors[state[i + 1]]:
                new_element = numbers_grid_neighbors[state[i + 1]][state[i]]
        new_state = state[: i + 1] + (new_element,) + state[i + 2 :]
        neighbors.add(new_state)

        # if s2 == "A" and s3 != "A" and s3 in numbers_grid_neighbors[s4]:
        # neighbors.add((s2, s3, numbers_grid_neighbors[s4][s3]))

    memo[state] = neighbors
    return neighbors


def get_steps(
    state: tuple[str, ...],
    target: tuple[str, ...],
    arrows_grid_neighbors,
    numbers_grid_neighbors,
) -> int:
    q = [(0, state)]
    seen = set()
    memo = {}
    while len(q) > 0:
        if len(q) % 1000 == 0:
            print(len(q))
        cost, state = q.pop(0)
        if state == target:
            return cost
        seen.add(state)
        ns = get_neighbors(state, arrows_grid_neighbors, numbers_grid_neighbors, memo)
        q.extend([(cost + 1, n) for n in ns if n not in seen])

    raise Exception("impossible state")


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    numbers_grid_data = ["789", "456", "123", "#0A"]
    numbers_grid = {
        (x, y): c
        for (y, line) in enumerate(numbers_grid_data)
        for (x, c) in enumerate(line)
        if c != "#"
    }

    arrows_grid_data = ["#^A", "<v>"]
    arrows_grid = {
        (x, y): c
        for (y, line) in enumerate(arrows_grid_data)
        for (x, c) in enumerate(line)
        if c != "#"
    }

    numbers_grid_neighbors = {}
    for k, v in numbers_grid.items():
        ns = get_neighbors_grid(k, numbers_grid)
        numbers_grid_neighbors[v] = {dir: numbers_grid[v] for dir, v in ns.items()}

    arrows_grid_neighbors = {}
    for k, v in arrows_grid.items():
        ns = get_neighbors_grid(k, arrows_grid)
        arrows_grid_neighbors[v] = {dir: arrows_grid[v] for dir, v in ns.items()}

    # print(numbers_grid_neighbors)
    # print(arrows_grid_neighbors)
    robots = 3
    state = ("A",) * robots
    ans = 0
    complexities = []
    for code in data:
        steps = 0
        for c in code:
            target = ("A",) * (robots - 1) + (c,)
            # get to number
            steps += get_steps(
                state, target, arrows_grid_neighbors, numbers_grid_neighbors
            )
            # press A
            steps += 1

            # print(f"{state} -> {target}: {steps} (total {ans})")
            state = target
        complexities.append(steps * int("".join(c for c in code if c.isnumeric())))
    ans = sum(complexities)
    print(ans)
    return ans


@cache
def get_steps2(robots: int, state: tuple[str, ...], target: str, presses: int):
    if presses == 0:
        return state, 0
    if len(state) == 0:
        return state, presses

    total_moves = 0
    current_grid = numbers_grid if len(state) == robots else arrows_grid
    current_grid_rev = numbers_grid_rev if len(state) == robots else arrows_grid_rev
    current_point = current_grid_rev[state[len(state) - 1]]
    target_point = current_grid_rev[target]

    dx = target_point[0] - current_point[0]
    dy = target_point[1] - current_point[1]
    target_horizontal = target_point[0], current_point[1]
    target_vertical = current_point[0], target_point[1]

    # if going horizontal would go to dead space, go vertical first then horizontal
    if target_horizontal not in current_grid:
        new_target = "v" if dy > 0 else "^"
        state, moves = get_steps2(robots, state[:-1], new_target, abs(dy))
        state += (target,)
        total_moves += moves

        new_target = ">" if dx > 0 else "<"
        state, moves = get_steps2(robots, state[:-1], new_target, abs(dx))
        state += (target,)
        total_moves += moves
    elif target_vertical not in current_grid:
        new_target = ">" if dx > 0 else "<"
        state, moves = get_steps2(robots, state[:-1], new_target, abs(dx))
        state += (target,)
        total_moves += moves

        new_target = "v" if dy > 0 else "^"
        state, moves = get_steps2(robots, state[:-1], new_target, abs(dy))
        state += (target,)
        total_moves += moves
    else:
        # try both orders and use best
        new_target = ">" if dx > 0 else "<"
        state_horizontal_first, moves_horizontal_first = get_steps2(
            robots, state[:-1], new_target, abs(dx)
        )
        state_horizontal_first += (target,)

        new_target = "v" if dy > 0 else "^"
        state_horizontal_first, moves = get_steps2(
            robots, state_horizontal_first[:-1], new_target, abs(dy)
        )
        state_horizontal_first += (target,)
        moves_horizontal_first += moves

        state_horizontal_first, moves = get_steps2(
            robots, state_horizontal_first[:-1], "A", presses
        )
        state_horizontal_first += (target,)
        total_moves_horizontal_first = total_moves + moves_horizontal_first + moves

        new_target = "v" if dy > 0 else "^"
        state_vertical_first, moves_vertical_first = get_steps2(
            robots, state[:-1], new_target, abs(dy)
        )
        state_vertical_first += (target,)

        new_target = ">" if dx > 0 else "<"
        state_vertical_first, moves = get_steps2(
            robots, state_vertical_first[:-1], new_target, abs(dx)
        )
        state_vertical_first += (target,)
        moves_vertical_first += moves

        state_vertical_first, moves = get_steps2(
            robots, state_vertical_first[:-1], "A", presses
        )
        state_vertical_first += (target,)
        total_moves_vertical_first = total_moves + moves_vertical_first + moves

        if total_moves_vertical_first < total_moves_horizontal_first:
            return state_vertical_first, total_moves_vertical_first
        else:
            return state_horizontal_first, total_moves_horizontal_first

    state, moves = get_steps2(robots, state[:-1], "A", presses)
    state += (target,)
    total_moves += moves
    return state, total_moves


numbers_grid_data = ["789", "456", "123", "#0A"]
numbers_grid = {
    (x, y): c
    for (y, line) in enumerate(numbers_grid_data)
    for (x, c) in enumerate(line)
    if c != "#"
}

arrows_grid_data = ["#^A", "<v>"]
arrows_grid = {
    (x, y): c
    for (y, line) in enumerate(arrows_grid_data)
    for (x, c) in enumerate(line)
    if c != "#"
}
numbers_grid_rev = {c: (x, y) for (x, y), c in numbers_grid.items()}
arrows_grid_rev = {c: (x, y) for (x, y), c in arrows_grid.items()}


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")

    robots = 26
    state = ["A"] * robots
    ans = 0
    complexities = []
    for code in data:
        steps = 0
        for c in code:
            # print(f"calling with {state}, target {c}")
            # get to number
            new_state, steps_needed = get_steps2(robots, tuple(state), c, 1)
            # print(steps_needed)
            steps += steps_needed
            state = new_state
        complexities.append(steps * int("".join(c for c in code if c.isnumeric())))
    ans = sum(complexities)
    print(ans)
    return ans


task1()
task2()
