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


def get_score(grid, start):
    peaks = set()

    def dfs(r, c, prev_value, visited):
        if not in_grid(r, c, grid):
            return
        if (r, c) in visited:
            return
        if grid[r][c] != prev_value + 1:
            return
        if grid[r][c] == 9:
            peaks.add((r, c))
            return

        for dr, dc in DIRS4:
            dfs(r + dr, c + dc, grid[r][c], visited | {(r, c)})

    dfs(start[0], start[1], -1, set())
    return len(peaks)


def get_score_2(grid, start):
    peaks = defaultdict(int)

    def dfs(r, c, prev_value, visited):
        if not in_grid(r, c, grid):
            return
        if (r, c) in visited:
            return
        if grid[r][c] != prev_value + 1:
            return
        if grid[r][c] == 9:
            peaks[(r, c)] += 1
            return

        for dr, dc in DIRS4:
            dfs(r + dr, c + dc, grid[r][c], visited | {(r, c)})

    dfs(start[0], start[1], -1, set())
    return sum(peaks.values())


def main():
    grid = get_grid("input")
    starts = get_starts(grid)
    print(sum(map(lambda x: get_score(grid, x), starts)))
    print(sum(map(lambda x: get_score_2(grid, x), starts)))


if __name__ == "__main__":
    main()
