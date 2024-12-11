import itertools


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


def get_answer(stones):
    N = 25
    converted_stones = stones
    for _ in range(N):
        s = list(map(convert, converted_stones))
        converted_stones = list(itertools.chain.from_iterable(s))

    return len(converted_stones)


def main():
    stones = get_stones("input")
    print(stones)
    print(get_answer(stones))


if __name__ == "__main__":
    main()
