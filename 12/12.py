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
    return [[x for x in line] for line in data]


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_plots(grid):
    plots = defaultdict(set)
    visited = set()

    def dfs(i, j, i0, j0, label):
        if not in_grid(i, j, grid):
            return
        if (i, j) in plots[(i0, j0)]:
            return
        if grid[i][j] != label:
            return

        plots[(i0, j0)].add((i, j))

        for dir in DIRS4:
            di, dj = dir
            dfs(i + di, j + dj, i0, j0, label)

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                dfs(r, c, r, c, grid[r][c])
                visited.update(plots[(r, c)])

    return plots


def get_perimeter(grid, plot_set):

    def get_count(n):
        count = 0
        r, c = n
        for dir in DIRS4:
            dr, dc = dir
            nr, nc = r + dr, c + dc
            if in_grid(nr, nc, grid) and (nr, nc) in plot_set:
                count += 1
        return 4 - count

    perimeter = 0
    for node in plot_set:
        perimeter += get_count(node)
    return perimeter


def get_answer(grid):
    plots = get_plots(grid)
    res = 0
    for plot_start, plot_set in plots.items():
        res += len(plot_set) * get_perimeter(grid, plot_set)
    return res


def main():
    grid = get_grid("input")
    print(get_answer(grid))


if __name__ == "__main__":
    main()
