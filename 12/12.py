from collections import defaultdict
from itertools import groupby
from operator import itemgetter

DIRS4 = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)

DIRS4_dict = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


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


def get_sides_number(plot_set):
    sides = defaultdict(list)
    for r, c in plot_set:
        for key, dir in DIRS4_dict.items():
            dr, dc = dir
            nr, nc = r + dr, c + dc
            if not (nr, nc) in plot_set:
                sides[key].append((r, c))
    # print(f"{sides=}")

    res = 0
    for key, value in sides.items():
        if key in {"UP", "DOWN"}:
            n1, n2 = 0, 1
        else:
            n1, n2 = 1, 0

        sorted_value = sorted(value, key=itemgetter(n1), reverse=True)
        # print(f"{key=} {sorted_value=}")

        for k, group in groupby(sorted_value, lambda x: x[n1]):
            group = list(group)
            # print(k, group)
            mapped = sorted(map(lambda x: x[n2], group))
            # print(k, mapped)
            c = 1
            prev = mapped[0]
            for i in mapped[1:]:
                if prev + 1 != i:
                    c += 1
                prev = i
            # print(f"{c=}")
            res += c

    return res


def get_answer_2(grid):
    plots = get_plots(grid)
    res = 0
    for plot_start, plot_set in plots.items():
        res += len(plot_set) * get_sides_number(plot_set)
    return res


def main():
    grid = get_grid("input")
    print(get_answer(grid))
    print(get_answer_2(grid))


if __name__ == "__main__":
    main()
