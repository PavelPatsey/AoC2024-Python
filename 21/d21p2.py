import cProfile
from functools import cache
from typing import List

DIRS4_dict = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

NUM_KP = (
    "789",
    "456",
    "123",
    "#0A",
)

DIR_KP = (
    "#^A",
    "<v>",
)


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def in_keypad(r, c, keypad):
    rows = len(keypad)
    cols = len(keypad[0])
    return 0 <= r < rows and 0 <= c < cols


def get_start(keypad):
    if keypad == NUM_KP:
        return 3, 2
    elif keypad == DIR_KP:
        return 0, 2
    else:
        raise Exception("Invalid keypad!")


@cache
def get_char_coords(char, keypad):
    rows = len(keypad)
    cols = len(keypad[0])
    for r in range(rows):
        for c in range(cols):
            if keypad[r][c] == char:
                return r, c
    assert False


def get_dist(start, end):
    """Manhattan distance"""
    sr, sc = start
    er, ec = end
    return abs(er - sr) + abs(ec - sc)


@cache
def possible_seqs(char_start, char_end, keypad):
    """
    Получить последовательности соответствующие Manhattan distance,
    при этом можно делать на больше одной смены направления, чтобы кнопки повторялись
    """
    start = get_char_coords(char_start, keypad)
    end = get_char_coords(char_end, keypad)
    max_dist = get_dist(start, end)
    possible_seqs = []

    def dfs(r, c, seq):
        if len(seq) > max_dist:
            return
        if not in_keypad(r, c, keypad):
            return
        if keypad[r][c] == "#":
            return
        if keypad[r][c] == char_end:
            assert len(seq) == max_dist
            possible_seqs.append(seq + "A")
        for key, drt in DIRS4_dict.items():
            dr, dc = drt
            nr, nc = r + dr, c + dc
            dfs(nr, nc, seq + key)

    dfs(start[0], start[1], "")
    return possible_seqs


@cache
def get_dir_length(char_start, char_end, keypad):
    start = get_char_coords(char_start, keypad)
    end = get_char_coords(char_end, keypad)
    return get_dist(start, end) + 1


@cache
def compute_length_recursion(seq, depth):
    if depth == 1:
        return sum(get_dir_length(x, y, DIR_KP) for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        possible_lengths = (
            compute_length_recursion(subseq, depth - 1)
            for subseq in possible_seqs(x, y, DIR_KP)
        )
        min_length = min(possible_lengths)
        print(f"{min_length=}")
        length += min_length
    return length


def convert_code(code, keypad) -> List:
    """Из кода получить возможные последовательности"""
    converted_seqs = [""]
    for x, y in zip("A" + code, code):
        all_char_seqs = possible_seqs(x, y, keypad)
        new_converted_seq = []
        for code in converted_seqs:
            for char_seq in all_char_seqs:
                new_converted_seq.append(code + char_seq)
        converted_seqs = new_converted_seq
    return converted_seqs


def answer(codes, depth):
    res = 0
    for code in codes:
        seqs = convert_code(code, NUM_KP)
        print(f"{seqs=}")
        length = min(map(lambda x: compute_length_recursion(x, depth), seqs))
        print(f"{length=} {int(code[:-1])=}")
        res += length * int(code[:-1])
    return res


def main():
    file = "input.txt"
    codes = get_data(file)
    ans1 = answer(codes, 2)
    print(f"{ans1=}")
    # ans2 = answer(codes, 25)
    # print(f"{ans1=}")


if __name__ == "__main__":
    assert get_dist((3, 2), (1, 1)) == 3

    assert possible_seqs("A", "0", NUM_KP) == ["<A"]
    assert possible_seqs("A", "A", NUM_KP) == ["A"]
    assert possible_seqs("A", "<", DIR_KP) == ["v<<A", "<v<A"]
    assert possible_seqs("0", "9", NUM_KP) == ["^^^>A", "^^>^A", "^>^^A", ">^^^A"]

    cProfile.run("main()")
