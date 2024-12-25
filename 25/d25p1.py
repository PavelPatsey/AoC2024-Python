def get_items(input_file):
    with open(input_file, "r") as file:
        items = file.read().strip().split("\n\n")
    items = [x.split() for x in items]
    return items


def convert_item(grid):
    rows = len(grid)
    cols = len(grid[0])
    lst = [0] * cols
    is_lock = "." not in grid[0]
    for r in range(rows):
        for c in range(cols):
            lst[c] += 1 if grid[r][c] == "#" else 0
    lst = [x - 1 for x in lst]
    heights = tuple(lst)
    return heights, is_lock


def made_locks_keys(items):
    locks = []
    keys = []
    for item in items:
        heights, is_lock = convert_item(item)
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)
    return locks, keys


def get_answer():
    pass


def main():
    file = "test_input.txt"
    items = get_items(file)
    print(items)
    locks, keys = made_locks_keys(items)
    print(f"{locks=}")
    print(f"{keys=}")


if __name__ == "__main__":
    test_item = ["#####", ".####", ".####", ".####", ".#.#.", ".#...", "....."]
    assert convert_item(test_item) == ((0, 5, 3, 4, 3), True)
    main()
