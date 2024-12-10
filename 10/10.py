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
            node = r, c
            peaks.add(node)
            return

        for new_dir in DIRS4:
            dr, dc = new_dir
            new_r = r + dr
            new_c = c + dc
            visited_node = r, c
            new_visited = visited | {visited_node}
            value = grid[r][c]
            dfs(new_r, new_c, value, new_visited)

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
            node = r, c
            peaks[node] += 1
            return

        for new_dir in DIRS4:
            dr, dc = new_dir
            new_r = r + dr
            new_c = c + dc
            visited_node = r, c
            new_visited = visited | {visited_node}
            value = grid[r][c]
            dfs(new_r, new_c, value, new_visited)

    dfs(start[0], start[1], -1, set())
    return sum(peaks.values())


def main():
    grid = get_grid("input")
    starts = get_starts(grid)
    print(sum(get_score(grid, node) for node in starts))
    print(sum(get_score_2(grid, node) for node in starts))


if __name__ == "__main__":
    main()
