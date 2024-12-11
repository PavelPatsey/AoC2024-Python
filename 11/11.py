import itertools
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

    return reduce((lambda x, acc: x + acc), converted_stones, 0)


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

    res = 0
    for s in stones:
        res += recursion(s, n)
    return res


def main():
    stones = get_stones("input")
    print(get_answer(stones, 25))
    print(get_answer_2(stones, 75))


if __name__ == "__main__":
    main()
