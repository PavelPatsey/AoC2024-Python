DIRS4 = {
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
}


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


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def dfs(grid, r, c, prev_value, visited):
    if not in_grid(r, c, grid):
        return 0
    if (r, c) in visited:
        return 0
    if grid[r][c] != prev_value + 1:
        return 0
    if grid[r][c] == 9:
        return 1

    res = 0
    for new_dir in DIRS4:
        dr, dc = new_dir
        new_r = r + dr
        new_c = c + dc
        visited_node = r, c
        new_visited = visited | {visited_node}
        value = grid[r][c]
        res += dfs(grid, new_r, new_c, value, new_visited)

    return res


def get_answer(grid):
    starts = get_starts(grid)
    print(f"{starts=}")

    for node in starts:
        r, c = node
        score = dfs(grid, r, c, -1, set())
        print(f"{score=}")
    return


def main():
    grid = get_grid("test_input_2")
    print(grid)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
