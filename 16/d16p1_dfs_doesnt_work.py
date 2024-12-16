import sys
from functools import cache

sys.setrecursionlimit(5_000)


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


DIRS4 = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


def rotate_clockwise(dir):
    return dir[1], -dir[0]


def rotate_counterclockwise(dir):
    return -dir[1], dir[0]


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                return r, c
    return


def dfs(grid, node, dir, score, visited):
    r, c = node
    if grid[r][c] == "E":
        return score
    elif grid[r][c] == "#" or node in visited:
        return float("inf")

    visited = visited | {node}

    dirs = [dir, rotate_clockwise(dir), rotate_counterclockwise(dir)]
    d_scores = [1, 1_001, 1_001]
    m = float("inf")
    for dir, ds in zip(dirs, d_scores):
        dr, dc = dir
        new_node = r + dr, c + dc
        new_score = score + ds
        a = dfs(grid, new_node, dir, new_score, visited)
        m = min(m, a)
    return m


def get_answer(grid):

    res = float("inf")
    start = get_start(grid)
    dir = (0, 1)
    dirs = [
        dir,
        rotate_clockwise(dir),
        rotate_counterclockwise(dir),
        rotate_clockwise(rotate_clockwise(dir)),
    ]
    scores = [1, 1_001, 1_001, 2_001]
    r, c = start
    for dir, score in zip(dirs, scores):
        dr, dc = dir
        new_node = r + dr, c + dc
        res = min(res, dfs(grid, new_node, dir, score, {start}))
    return res


def main():
    grid = get_data("input_large.txt")
    print(get_answer(grid))


if __name__ == "__main__":
    main()
