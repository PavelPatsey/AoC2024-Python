import cProfile
from collections import Counter, deque
from copy import deepcopy

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
            if (
                r != 0
                and r != rows - 1
                and c != 0
                and c != cols - 1
                and grid[r][c] == "#"
            ):
                walls.add((r, c))
    return walls


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_max_score(grid, start):
    sr, sc = start
    visited = set()
    queue = deque()
    queue.append((0, sr, sc))

    while queue:
        node = queue.popleft()
        score, r, c = node

        if grid[r][c] == "E":
            return score

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1

            if grid[nr][nc] != "#" and (nr, nc) not in visited:
                queue.append((new_score, nr, nc))
                visited.add((nr, nc))

    return


def get_score_with_limit(grid, start, score_limit):
    sr, sc = start
    visited = set()
    queue = deque()
    queue.append((0, sr, sc))
    res = None

    while queue:
        node = queue.popleft()
        score, r, c = node

        if grid[r][c] == "E":
            res = score
            break

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1

            if (
                grid[nr][nc] != "#"
                and (nr, nc) not in visited
                and new_score <= score_limit
            ):
                queue.append((new_score, nr, nc))
                visited.add((nr, nc))

    return res


def get_answer(grid, save):
    start = get_start(grid)
    max_score = get_max_score(grid, start)
    score_limit = max_score - save
    print(f"{max_score=}")
    print(f"{score_limit=}")
    walls = get_walls(grid)
    print(f"{len(walls)=}")
    res = []
    i = 0
    for r, c in walls:
        new_grid = deepcopy(grid)
        new_grid[r][c] = "."
        score = get_score_with_limit(new_grid, start, score_limit)
        # print(f"{score=}")
        if score:
            res.append(score)
        i += 1
        if i % 100 == 0:
            print(f"{i=} {score=}")

    counter = Counter(res)
    print(counter)
    print(sorted(counter.values()))
    return sum(counter.values())


def main():
    # file = "test_input.txt"
    # save = 1

    file = "input.txt"
    save = 100

    grid = get_data(file)
    print(get_answer(grid, save))


if __name__ == "__main__":
    cProfile.run("main()")
