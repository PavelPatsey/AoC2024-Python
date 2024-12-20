import cProfile
import heapq
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


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                return r, c
    return


def get_walls(grid):
    walls = set()
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                walls.add((r, c))
    return walls


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_score(grid, start):
    sr, sc = start
    visited = set()
    queue = deque()
    queue.append((0, sr, sc))

    while queue:
        node = queue.popleft()
        score, r, c = node

        if grid[r][c] == "E":
            res = score
            break

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1
            new_item = new_score, nr, nc

            if grid[nr][nc] != "#" and new_item not in visited:
                queue.append(new_item)
                visited.add(new_item)

    return res


def get_scores_less_than_limit(grid, start, score_limit):
    res = []
    sr, sc = start
    visited = set()
    queue = deque()
    queue.append((0, sr, sc, 1))

    while queue:
        node = queue.popleft()
        score, r, c, cheat = node
        # print(f"{item=}")

        if grid[r][c] == "E":
            print(f"{score=}")
            res.append(score)

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1
            new_cheat = cheat
            if in_grid(nr, nc, grid) and grid[nr][nc] == "#":
                new_cheat -= 1
            new_node = new_score, nr, nc, new_cheat

            if (
                in_grid(nr, nc, grid)
                and (grid[nr][nc] != "#" or grid[nr][nc] == "#" and new_cheat >= 0)
                and new_node not in visited
                and new_score < score_limit
            ):
                queue.append(new_node)
                visited.add(new_node)

    print(f"{res=}")
    mapped = list(sorted(map(lambda x: score_limit - x, res)))
    print(f"{mapped=}")
    return mapped


def get_answer(grid):
    start = get_start(grid)
    score_limit = get_score(grid, start)
    print(f"{score_limit=}")
    res = get_scores_less_than_limit(grid, start, score_limit)
    return res


def main():
    file = "test_input.txt"
    grid = get_data(file)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
