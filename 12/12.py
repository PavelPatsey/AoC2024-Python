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


def get_plots_dfs(grid):
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


def get_plots_bfs(grid):
    visited_plots = set()
    plots = defaultdict(set)

    def bfs(node, label, grid):
        visited = {node}
        queue = [node]
        while queue:
            i, j = queue.pop()
            for di, dj in DIRS4:
                ni, nj = i + di, j + dj
                if (
                    in_grid(ni, nj, grid)
                    and (ni, nj) not in visited
                    and grid[ni][nj] == label
                ):
                    queue.append((ni, nj))
                    visited.add((ni, nj))
        return visited

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited_plots:
                plot_set = bfs((r, c), grid[r][c], grid)
                plots[(r, c)] = plot_set
                visited_plots.update(plot_set)

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

    return sum(map(get_count, plot_set))


def get_sides_number(plot_set):
    def _get_sides(plot_set):
        sides = defaultdict(list)
        for r, c in plot_set:
            for key, dir in DIRS4_dict.items():
                dr, dc = dir
                nr, nc = r + dr, c + dc
                if not (nr, nc) in plot_set:
                    sides[key].append((r, c))
        return sides

    def _get_gaps_count(numbers):
        count = 1
        prev = numbers[0]
        for i in numbers[1:]:
            if i != prev + 1:
                count += 1
            prev = i
        return count

    sides = _get_sides(plot_set)
    res = 0
    for key, value in sides.items():
        if key in {"UP", "DOWN"}:
            s_index, g_index = 0, 1
        else:
            s_index, g_index = 1, 0

        sorted_value = sorted(value, key=itemgetter(s_index), reverse=True)

        for _, group in groupby(sorted_value, itemgetter(s_index)):
            sorted_mapped = sorted(map(itemgetter(g_index), group))
            count = _get_gaps_count(sorted_mapped)
            res += count

    return res


def main():
    grid = get_grid("input")

    plots_dfs = get_plots_dfs(grid)
    ans1_dfs = sum(map(lambda x: len(x) * get_perimeter(grid, x), plots_dfs.values()))
    print(ans1_dfs)

    plots_bfs = get_plots_bfs(grid)
    ans1_bfs = sum(map(lambda x: len(x) * get_perimeter(grid, x), plots_bfs.values()))
    print(ans1_bfs)

    ans2 = sum(map(lambda x: len(x) * get_sides_number(x), plots_bfs.values()))
    print(ans2)

    assert ans1_dfs == 1424006
    assert ans1_bfs == 1424006
    assert ans2 == 858684


if __name__ == "__main__":
    main()
