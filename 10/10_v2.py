from collections import defaultdict

DIRS4 = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


def get_grid(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    grid = [[int(x) if x.isdigit() else -1 for x in line] for line in data]
    return grid


def get_starts(grid):
    rows = len(grid)
    cols = len(grid[0])
    starts = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                starts.append((r, c))
    return tuple(starts)


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_score(grid, start, collect=set):
    def dfs(r, c, prev_value):
        if not in_grid(r, c, grid):
            return
        if grid[r][c] != prev_value + 1:
            return
        if grid[r][c] == 9:
            yield r, c

        for dr, dc in DIRS4:
            yield from dfs(r + dr, c + dc, grid[r][c])

    return len(collect(dfs(start[0], start[1], -1)))


def main():
    grid = get_grid("input")
    starts = get_starts(grid)
    print(sum(map(lambda x: get_score(grid, x), starts)))
    print(sum(map(lambda x: get_score(grid, x, list), starts)))


if __name__ == "__main__":
    main()
