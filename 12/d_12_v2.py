from collections import defaultdict
from functools import reduce
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





def get_corners_number(plot_set):

    return 0


def main():
    grid = get_grid("input")

    plots_bfs = get_plots_bfs(grid)
    ans1_bfs = sum(map(lambda x: len(x) * get_perimeter(grid, x), plots_bfs.values()))
    print(ans1_bfs)

    ans2 = sum(map(lambda x: len(x) * get_corners_number(x), plots_bfs.values()))
    print(ans2)

    assert ans1_bfs == 1424006
    assert ans2 == 858684


if __name__ == "__main__":
    main()
