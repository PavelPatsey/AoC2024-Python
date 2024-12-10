def get_grid(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    grid = [[int(x) if x.isdigit() else -1 for x in line] for line in data]
    return grid


def get_starts(grid):
    rows = len(grid)
    cols = len(grid[0])
    starts = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                starts.add((r, c))
    return starts


def get_answer(grid):
    starts = get_starts(grid)
    print(starts)


def main():
    grid = get_grid("test_input_1")
    print(grid)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
