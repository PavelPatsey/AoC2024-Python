import cProfile
import heapq
from collections import Counter, deque
from copy import deepcopy
from functools import cache

DIRS4 = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


def get_start_end(grid):
    start, end = None, None
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = r, c
            if grid[r][c] == "E":
                end = r, c
    return start, end


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_scores_from(grid, start):
    sr, sc = start
    scores_dict = {}
    queue = deque()
    queue.append((0, sr, sc))

    while queue:
        node = queue.popleft()
        score, r, c = node

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1

            if grid[nr][nc] != "#" and (nr, nc) not in scores_dict:
                queue.append((new_score, nr, nc))
                scores_dict[(nr, nc)] = new_score

    return scores_dict


def get_score_from_to(grid, start, end):
    sr, sc = start
    visited = set()
    queue = deque()
    queue.append((0, sr, sc))

    while queue:
        node = queue.popleft()
        score, r, c = node

        if (r, c) == end:
            return score

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1

            if grid[nr][nc] != "#" and (nr, nc) not in visited:
                queue.append((new_score, nr, nc))
                visited.add((nr, nc))

    return


def get_dirs(manh_dist_limit):
    dirs = set()
    for i in range(manh_dist_limit + 1):
        for j in range(manh_dist_limit + 1):
            if 0 < i + j <= manh_dist_limit:
                dirs.add((i, j))
    return dirs


def get_answer(grid, save, manh_dist_limit):
    start, end = get_start_end(grid)
    scores_from_start = get_scores_from(grid, start)
    scores_from_end = get_scores_from(grid, end)
    base_score = scores_from_start[(end[0], end[1])]
    assert scores_from_start[(end[0], end[1])] == base_score
    score_limit = base_score - save

    dirs = get_dirs(manh_dist_limit)
    res = []

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            p1 = (r, c)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if in_grid(nr, nc, grid):
                    p2 = (nr, nc)
                score = (
                    scores_from_start[p1]
                    + get_score_from_to(grid, p1, p2)
                    + scores_from_end[p2]
                )
                if score <= score_limit:
                    res.append(score)
    counter = Counter(res)
    print(counter)
    print(sorted(counter.values()))
    return sum(counter.values())


def main():
    file = "test_input.txt"
    save = 1

    # file = "input.txt"
    # save = 100

    grid = get_data(file)
    manh_dist_limit = 1
    print(get_answer(grid, save, manh_dist_limit))


if __name__ == "__main__":
    main()
    # cProfile.run("main()")
