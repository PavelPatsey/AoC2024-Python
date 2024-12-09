import itertools
from functools import cache


def get_stones(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    stones = [int(x) for x in data.split()]
    return stones


def convert(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        l = len(stone_str)
        return [int(stone_str[0 : l // 2]), int(stone_str[l // 2 :])]
    else:
        return [stone * 2024]


def get_answer(stones, n):
    N = n
    converted_stones = stones
    for i in range(N):
        s = map(convert, converted_stones)
        converted_stones = itertools.chain.from_iterable(s)

    return len(list(converted_stones))


def get_answer_2(stones, n):

    @cache
    def backtrack(stone, steps):
        if steps == 0:
            return 1
        if stone == 0:
            return backtrack(1, steps - 1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            l = len(stone_str)
            left, right = int(stone_str[0 : l // 2]), int(stone_str[l // 2 :])
            return backtrack(left, steps - 1) + backtrack(right, steps - 1)
        else:
            return backtrack(stone * 2024, steps - 1)

    res = 0
    for s in stones:
        res += backtrack(s, n)
    return res


def main():
    stones = get_stones("input")
    print(get_answer(stones, 25))
    print(get_answer_2(stones, 75))


if __name__ == "__main__":
    main()
