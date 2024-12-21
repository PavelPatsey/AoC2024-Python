import cProfile
from functools import cache
from typing import List, Set

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
def get_end(char, keypad):
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
def dfs(start, char, keypad) -> List:
    """Получить последовательности соответствующие Manhattan distance"""
    end = get_end(char, keypad)
    max_dist = get_dist(start, end)
    all_seqs = []

    def _dfs(r, c, seq):
        if len(seq) > max_dist:
            return
        if not in_keypad(r, c, keypad):
            return
        if keypad[r][c] == "#":
            return
        if keypad[r][c] == char:
            assert len(seq) == max_dist
            all_seqs.append(seq + "A")
        for key, drt in DIRS4_dict.items():
            dr, dc = drt
            nr, nc = r + dr, c + dc
            _dfs(nr, nc, seq + key)

    _dfs(start[0], start[1], "")
    return all_seqs, end


def get_len_without_duplicates(seq):
    """Получить длину без дубликатов"""
    prev = seq[0]
    res = 1
    for curr in seq[1:]:
        if curr != prev:
            res += 1
        prev = curr
    return res

    # f = get_len_without_duplicates
    # mapped = list(map(lambda x: (f(x), x), all_seqs))
    # print(f"{mapped=}")


def convert_seq(seq, keypad) -> List:
    """Из одной последовательности получить возможные последовательности"""
    start = get_start(keypad)
    converted_seqs = [""]
    for char in seq:
        all_char_seqs, start = dfs(start, char, keypad)
        new_converted_seq = []
        for seq in converted_seqs:
            for char_seq in all_char_seqs:
                new_converted_seq.append(seq + char_seq)
        converted_seqs = new_converted_seq
    return converted_seqs


def convert_code(code):
    conv_seqs_1 = convert_seq(code, NUM_KP)

    conv_seqs_2 = []
    for seq_1 in conv_seqs_1:
        conv_seqs_2.extend(convert_seq(seq_1, DIR_KP))

    conv_seqs_3 = []
    for seq_2 in conv_seqs_2:
        conv_seqs_3.extend(convert_seq(seq_2, DIR_KP))

    min_len = float("inf")
    for seq_3 in conv_seqs_3:
        min_len = min(min_len, len(seq_3))

    code_num = int(code[:-1])
    return code_num * min_len


def main():
    file = "input.txt"
    codes = get_data(file)
    ans1 = sum(map(convert_code, codes))
    print(f"{ans1=}")


if __name__ == "__main__":
    assert get_dist((3, 2), (1, 1)) == 3

    assert get_len_without_duplicates("123") == 3
    assert get_len_without_duplicates("1233") == 3
    assert get_len_without_duplicates("A^A^>^AvvvA") == 9

    assert dfs(get_start(NUM_KP), "0", NUM_KP) == (["<A"], (3, 1))
    assert dfs(get_start(NUM_KP), "A", NUM_KP) == (["A"], (3, 2))
    assert dfs(get_start(DIR_KP), "<", DIR_KP) == (["v<<A", "<v<A"], (1, 0))

    assert set(convert_seq("029A", NUM_KP)) == {
        "<A^A>^^AvvvA",
        "<A^A^>^AvvvA",
        "<A^A^^>AvvvA",
    }

    print("test 1")
    assert convert_code("029A") == 68 * 29
    print("test 2")
    assert convert_code("980A") == 60 * 980
    print("test 3")
    assert convert_code("179A") == 68 * 179
    print("test 4")
    assert convert_code("456A") == 64 * 456
    print("test 5")
    assert convert_code("379A") == 64 * 379

    print("start main()")
    cProfile.run("main()")
