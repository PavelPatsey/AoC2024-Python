from collections import deque
from functools import cache

DIRS4_dict = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

NUM_KP = [
    "789",
    "456",
    "123",
    "#0A",
]

DIR_KP = [
    "#^A",
    "<v>",
]


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


def bfs(start, char, keypad):
    sr, sc = start
    visited = {start}
    queue = deque([(sr, sc, "")])

    while queue:
        r, c, track = queue.popleft()
        if keypad[r][c] == char:
            # t_a = track + "A"
            # print(f"{t_a =}")
            return track + "A", (r, c)

        for key, drt in DIRS4_dict.items():
            dr, dc = drt
            nr, nc = r + dr, c + dc

            if (
                in_keypad(nr, nc, keypad)
                and keypad[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                new_track = track + key
                queue.append((nr, nc, new_track))
                visited.add((nr, nc))
    assert False


def convert(seq, keypad):
    new_start = get_start(keypad)
    converted_seq = ""
    for char in seq:
        converted_char, new_start = bfs(new_start, char, keypad)
        converted_seq += converted_char
    return converted_seq


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    codes = get_data(file)
    # print(codes)
    print(get_answer(codes))


if __name__ == "__main__":
    assert bfs(get_start(NUM_KP), "0", NUM_KP) == ("<A", (3, 1))
    assert bfs(get_start(NUM_KP), "A", NUM_KP) == ("A", (3, 2))

    assert bfs(get_start(DIR_KP), "<", DIR_KP) == ("v<<A", (1, 0))

    conv_seq = convert("029A", NUM_KP)
    assert conv_seq in {"<A^A>^^AvvvA", "<A^A^>^AvvvA", "<A^A^^>AvvvA"}

    conv_seq_2 = convert("v<<A>>^A<A>AvA<^AA>A<vAAA>^A", DIR_KP)
    test_res = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    assert len(conv_seq_2) == len(test_res)

    main()
