from collections import deque
from functools import cache

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
def dfs(start, char, keypad):
    """Получить последовательности соответствующие Manhattan distance"""
    sr, sc = start
    end = get_end(char, keypad)
    max_dist = get_dist(start, end)
    all_seqs = set()

    def _dfs(r, c, seq):
        if len(seq) > max_dist:
            return
        if not in_keypad(r, c, keypad):
            return
        if keypad[r][c] == "#":
            return
        if keypad[r][c] == char:
            assert len(seq) == max_dist
            all_seqs.add(seq + "A")
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


def convert_char(new_start, char, keypad):
    """Получить последовательности и выбрать самую короткую в перспективе"""
    all_seqs, end = bfs(new_start, char, keypad)


def convert_seq(seq, keypad):
    new_start = get_start(keypad)
    converted_seq = ""
    for char in seq:
        converted_char, new_start = bfs(new_start, char, keypad)
        converted_seq += converted_char
    return converted_seq


def convert_code(code):
    code = "029A"
    print(f"{code=}")

    converted_1 = convert_seq(code, NUM_KP)
    print(f"{converted_1=} {len(converted_1)=}")
    assert len(converted_1) == len("<A^A>^^AvvvA")

    converted_2 = convert_seq(converted_1, DIR_KP)
    print(f"{converted_2=} {len(converted_2)=}")
    assert len(converted_2) == len("v<<A>>^A<A>AvA<^AA>A<vAAA>^A")

    converted_3 = convert_seq(converted_2, DIR_KP)
    print(f"{converted_3=} {len(converted_3)=}")

    doljno_byt = len(
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    )
    # a 'v<A<AA>^>AvA^<Av>A^Av<<A>^>AvA^Av<<A>^>AAv<A>A^A<A>Av<A<A>^>AAA<Av>A^A'
    print(f"{doljno_byt=}")
    assert len(converted_3) == len(
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    )

    code_num = int(code[:-1])
    return code_num * len(converted_3)


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    codes = get_data(file)
    # print(codes)
    print(get_answer(codes))


if __name__ == "__main__":
    assert get_dist((3, 2), (1, 1)) == 3

    assert get_len_without_duplicates("123") == 3
    assert get_len_without_duplicates("1233") == 3

    assert dfs(get_start(NUM_KP), "0", NUM_KP) == ({"<A"}, (3, 1))
    assert dfs(get_start(NUM_KP), "A", NUM_KP) == ({"A"}, (3, 2))
    assert dfs(get_start(DIR_KP), "<", DIR_KP) == ({"v<<A", "<v<A"}, (1, 0))

    # conv_seq = convert_seq("029A", NUM_KP)
    # assert conv_seq in {"<A^A>^^AvvvA", "<A^A^>^AvvvA", "<A^A^^>AvvvA"}
    #
    # conv_seq_2 = convert_seq("v<<A>>^A<A>AvA<^AA>A<vAAA>^A", DIR_KP)
    # test_res = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    # assert len(conv_seq_2) == len(test_res)

    # print(convert_code("029A"))
    # print(68 * 29)
    # assert convert_code("029A") == 68 * 29
    # main()
