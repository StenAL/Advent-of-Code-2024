from util import *
from collections import *
import copy
from functools import reduce
from math import prod

day = 22


def mix(secret, n):
    return secret ^ n


def prune(n):
    return n % 16777216


def task1():
    data = get_int_input_for_day(day)
    # data = get_int_input_for_file("test")
    secrets = []
    for secret in data:
        loops = 2000
        for i in range(loops):
            secret = mix(secret, secret * 64)
            secret = prune(secret)

            secret = mix(secret, secret // 32)
            secret = prune(secret)

            secret = mix(secret, secret * 2048)
            secret = prune(secret)
        secrets.append(secret)
    ans = sum(secrets)
    print(ans)
    return ans


def task2():
    data = get_int_input_for_day(day)
    # data = get_int_input_for_file("test2")

    loops = 2000
    delta_sequence_earnings = defaultdict(int)
    for secret in data:
        prices = [int(str(secret)[-1])]
        changes = []
        for i in range(loops):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ (secret // 32)) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216

            prices.append(int(str(secret)[-1]))
            changes.append(prices[i + 1] - prices[i])

        seen_sequences = set()
        for i in range(3, len(changes)):
            s = (changes[i - 3], changes[i - 2], changes[i - 1], changes[i])
            if s in seen_sequences:
                continue
            seen_sequences.add(s)
            delta_sequence_earnings[s] += prices[i + 1]

    most_bananas = max(delta_sequence_earnings.values())
    ans = most_bananas
    print(ans)
    return ans


task1()
task2()
