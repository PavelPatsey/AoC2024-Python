import cProfile
from collections import deque

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
    scores_dict = {(sr, sc): 0}
    queue = deque([(0, sr, sc)])

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


def get_dirs(manh_dist_limit):
    dirs = set()
    for dr in range(-manh_dist_limit, manh_dist_limit + 1):
        for dc in range(-manh_dist_limit, manh_dist_limit + 1):
            if 1 < abs(dr) + abs(dc) <= manh_dist_limit:
                dirs.add((dr, dc))
    return dirs


def get_answer(grid, diff_max, manh_dist_limit):
    start, end = get_start_end(grid)
    scores_from_start = get_scores_from(grid, start)
    scores_from_end = get_scores_from(grid, end)
    base_score = scores_from_start[(end[0], end[1])]
    assert scores_from_start[(end[0], end[1])] == base_score
    assert scores_from_end[(start[0], start[1])] == base_score

    dirs = get_dirs(manh_dist_limit)
    res = 0

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            p1 = (r, c)
            if p1 not in scores_from_start:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                p2 = (nr, nc)
                if p2 not in scores_from_end:
                    continue
                start_p1 = scores_from_start[p1]
                p1_p2 = abs(dr) + abs(dc)
                p2_end = scores_from_end[p2]
                score = start_p1 + p1_p2 + p2_end
                if score < base_score:
                    diff = base_score - score
                    if diff >= diff_max:
                        res += 1

    return res


def main():
    # file = "test_input.txt"
    # diff_max = 0

    file = "input.txt"
    diff_max = 100

    grid = get_data(file)
    manh_dist_limit = 2

    ans1 = get_answer(grid, diff_max, manh_dist_limit)
    print(f"{ans1=}")

    manh_dist_limit = 20
    ans2 = get_answer(grid, diff_max, manh_dist_limit)
    print(f"{ans2=}")


if __name__ == "__main__":
    cProfile.run("main()")
