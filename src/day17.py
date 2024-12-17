from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 17

def get_combo_operand(operand, a, b, c) -> int:
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    print("error")
    return -1


def task1():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    registers_data, program_data = data
    a, b, c = (int(r.split(": ")[1]) for r in registers_data)
    program = [int(e) for e in program_data[0].split(": ")[1].split(",")]
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(program) - 1:
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        if instruction == 0:
            numerator = a
            denominator = 2 ** get_combo_operand(operand, a, b, c)
            a = numerator // denominator
            instruction_pointer += 2
        elif instruction == 1:
            result = b ^ operand
            b = result
            instruction_pointer += 2
        elif instruction == 2:
            b = get_combo_operand(operand, a, b, c) % 8
            instruction_pointer += 2
        elif instruction == 3:
            if a == 0:
                instruction_pointer += 2
            else:
                instruction_pointer = operand
        elif instruction == 4:
            b = b ^ c
            instruction_pointer += 2
        elif instruction == 5:
            output.append(get_combo_operand(operand, a, b, c) % 8)
            instruction_pointer += 2
        elif instruction == 6:
            numerator = a
            denominator = 2 ** get_combo_operand(operand, a, b, c)
            b = numerator // denominator
            instruction_pointer += 2
        elif instruction == 7:
            numerator = a
            denominator = 2 ** get_combo_operand(operand, a, b, c)
            c = numerator // denominator
            instruction_pointer += 2
    ans = ",".join(str(e) for e in output)
    print(ans)


def task2():
    data = get_grouped_input_for_day(day)
    # data = get_grouped_input_for_file("test")
    registers_data, program_data = data
    a, b, c = (int(r.split(": ")[1]) for r in registers_data)
    program = [int(e) for e in program_data[0].split(": ")[1].split(",")]
    # after 2,4 (idx 2: a=66752888, b=0, c=0)
    # after 1,7 (idx 4: a=66752888, b=7, c=0)
    # after 7,5 (idx 6: a=66752888, b=7, c=521506)
    # after 1,7 (idx 8: a=66752888, b=0, c=521506)
    # after 0,3 (idx 10: a=8344111, b=0, c=521506)
    # after 4,1 (idx 12: a=8344111, b=521506, c=521506)
    # after 5,5 (idx 14: a=8344111, b=521506, c=521506)
    # after 3,0 (idx 0: a=8344111, b=521506, c=521506)

    # 2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0
    # 1. (2,4) b = a % 8
    # 2. (1,7) b = b ^ 7
    # 3. (7,5) c = a / (2 ** b)
    # 4. (1,7) b = b ^ 7
    # 5. (0,3) a = a / (2 ** 3)
    # 6. (4,1) b = b ^ c
    # 7. (5,5) output b % 8
    # 8. (3,0) if a == 0 terminate, otherwise loop to start
    # each cycle, a gets divided by 8 => program length is 16, minimum value for a is 8 ** 16
    # each cycle, b = (a % 8) ^ 7 ^ 7 ^ c and c = a / 2 ** b = a / 2 ** ((a % 8) ^ 7)
    # b = (a % 8) ^ c 
    # c = a / 2 ** (7 - (a % 8))
    desired = program[::-1]
    start = 0
    digits = 0
    ans = -1
    while digits < len(program):
        digits += 1
        i = start
        # print(f"looking for {digits} digits ({desired[:digits][::-1]}) starting at {start}")
        while True:
            a = i 
            b = 0
            c = 0
            output = []
            while a > 0:
                c = a // (2 ** ((a % 8) ^ 7))
                b = (a % 8) ^ c
                out = b % 8
                output.append(out)
                a = a // 8
            if output == desired[:digits][::-1]:
                start = i * 8
                # print(f"found: {i}")
                break
            i += 1
        ans = i
    print(ans)


task1()
task2()
