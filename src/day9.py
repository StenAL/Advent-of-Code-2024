from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 9


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0]
    holes = deque()  # (index, length)
    data_chunks = deque()  # (id, start_index, length)
    data_index = 0
    for i in range(len(data)):
        c = int(data[i])
        if i % 2 == 0:
            data_chunks.append((i // 2, data_index, c))
        else:
            holes.append((data_index, c))
        data_index += c

    while len(holes) > 0:
        if holes[0][0] > data_chunks[-1][1]:
            holes.pop()
            continue
        chunk = data_chunks.pop()
        chunk_id, chunk_start, chunk_length = chunk
        hole = holes.popleft()
        hole_start, hole_length = hole
        if hole_length >= chunk_length:
            data_chunks.appendleft((chunk_id, hole_start, chunk_length))
            # print(f"A: move {chunk_id} (len {chunk_length}) to index {hole_start}, hole {hole}")
            if hole_length > chunk_length:
                holes.appendleft(
                    (hole_start + chunk_length, hole_length - chunk_length)
                )
        else:
            data_chunks.appendleft((chunk_id, hole_start, hole_length))
            data_chunks.append((chunk_id, chunk_start, chunk_length - hole_length))
            # print(f"B: move {chunk_id} (len {hole_length}) to index {hole_start}")

    ans = 0
    for chunk_id, chunk_start, chunk_length in data_chunks:
        for i in range(chunk_start, chunk_start + chunk_length):
            ans += i * chunk_id
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0]
    # data = "115" # 0.11111"
    holes = deque()  # (index, length)
    q = deque()  # (id, start_index, length)
    data_index = 0
    for i in range(len(data)):
        c = int(data[i])
        if i % 2 == 0:
            q.append((i // 2, data_index, c))
        elif c != 0:
            holes.append((data_index, c))
        data_index += c

    data_chunks = []
    while len(q) > 0:
        chunk = q.pop()
        chunk_id, chunk_start, chunk_length = chunk
        new_holes = []
        found_hole = False
        for hole in holes:
            hole_start, hole_length = hole
            if found_hole or hole_length < chunk_length or hole_start >= chunk_start:
                new_holes.append(hole)
            else:
                data_chunks.append((chunk_id, hole_start, chunk_length))
                if hole_length > chunk_length:
                    new_holes.append(
                        (hole_start + chunk_length, hole_length - chunk_length)
                    )
                found_hole = True

        holes = new_holes
        if not found_hole:
            data_chunks.append((chunk_id, chunk_start, chunk_length))

    ans = 0
    for chunk_id, chunk_start, chunk_length in data_chunks:
        for i in range(chunk_start, chunk_start + chunk_length):
            ans += i * chunk_id
    print(ans)
    return ans


def print_data(data_chunks):
    s = sorted(data_chunks, key=lambda x: x[1])
    last_chunk_end = 0
    for chunk_id, chunk_start, chunk_length in s:
        if last_chunk_end < chunk_start:
            print("." * (chunk_start - last_chunk_end), end="")
        print(str(chunk_id) * chunk_length, end="")
        last_chunk_end = chunk_start + chunk_length
    print()


task1()
task2()
