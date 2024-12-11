import itertools
import time
from collections import Counter
from functools import cache, reduce


def get_stones(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    stones = [int(x) for x in data.split()]
    return stones


def convert(stone):
    if stone == 0:
        yield 1
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        l = len(stone_str)
        yield int(stone_str[0 : l // 2])
        yield int(stone_str[l // 2 :])
    else:
        yield stone * 2024


def get_answer(stones, n):
    converted_stones = stones
    for _ in range(n):
        mapped = map(convert, converted_stones)
        converted_stones = itertools.chain.from_iterable(mapped)

    return reduce(lambda acc, x: acc + 1, converted_stones, 0)


def get_answer_2(stones, n):

    @cache
    def recursion(stone, steps):
        if steps == 0:
            return 1
        if stone == 0:
            return recursion(1, steps - 1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            l = len(stone_str)
            left, right = int(stone_str[0 : l // 2]), int(stone_str[l // 2 :])
            return recursion(left, steps - 1) + recursion(right, steps - 1)
        else:
            return recursion(stone * 2024, steps - 1)

    return sum(map(lambda x: recursion(x, n), stones))


def get_answer_3(stones, n):
    counter = Counter(stones)

    for _ in range(n):
        new_counter = Counter()
        for stone, number in counter.items():
            if stone == 0:
                new_counter[1] += number
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                l = len(stone_str)
                left = int(stone_str[0 : l // 2])
                right = int(stone_str[l // 2 :])
                new_counter[left] += number
                new_counter[right] += number
            else:
                new_counter[stone * 2024] += number
        counter = new_counter

    return sum(counter.values())


def main():
    stones = get_stones("input")

    t0 = time.time()

    print(get_answer(stones, 25))
    t1 = time.time()
    dt = t1 - t0
    print("dt1 =", "{:.2f}".format(dt), "sec")

    print(get_answer_2(stones, 75))
    t2 = time.time()
    dt = t2 - t1
    print("dt2 =", "{:.2f}".format(dt), "sec")

    print(get_answer_3(stones, 75))
    t3 = time.time()
    dt = t3 - t2
    print("dt3 =", "{:.2f}".format(dt), "sec")


if __name__ == "__main__":
    main()
