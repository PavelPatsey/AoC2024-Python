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


def is_overlapped(tuple_1, tuple_2, max_value):
    if not len(tuple_1) == len(tuple_2):
        raise Exception("the lengths do not match!")
    mapped = map(lambda x: x[0] + x[1] > max_value, zip(tuple_1, tuple_2))
    return any(mapped)


def answer(locks, keys):
    counter = 0
    for l in locks:
        for k in keys:
            if not is_overlapped(l, k, 5):
                counter += 1
    return counter


def main():
    file = "test_input.txt"
    items = get_items(file)
    locks, keys = made_locks_keys(items)
    asn1 = answer(locks, keys)
    print(f"{asn1=}")


if __name__ == "__main__":
    test_item = ["#####", ".####", ".####", ".####", ".#.#.", ".#...", "....."]
    assert convert_item(test_item) == ((0, 5, 3, 4, 3), True)
    main()
