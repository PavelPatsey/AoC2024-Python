from collections import deque

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


def bfs(start, end_symb, keypad):
    sr, sc = start
    visited = {start}
    queue = deque([(sr, sc, "")])

    while queue:
        r, c, track = queue.popleft()
        if keypad[r][c] == end_symb:
            # t_a = track + "A"
            # print(f"{t_a =}")
            return track + "A"

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
    sr, sc = get_start(keypad)
    pass


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    codes = get_data(file)
    # print(codes)
    print(get_answer(codes))


if __name__ == "__main__":
    assert bfs(get_start(NUM_KP), "0", NUM_KP) == "<A"
    assert bfs(get_start(NUM_KP), "A", NUM_KP) == "A"

    assert bfs(get_start(DIR_KP), "<", DIR_KP) == "v<<A"

    main()
