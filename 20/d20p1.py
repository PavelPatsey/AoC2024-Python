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


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_answer(grid):
    res = None
    sr, sc = get_start(grid)
    visited = set()
    queue = deque()
    queue.append((0, sr, sc, 0))

    while queue:
        item = queue.popleft()

        score, r, c, cheat = item
        print(f"{item=}")

        if grid[r][c] == "E":
            res = score
            break

        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1

            # if grid[nr][nc] != "#":
            #     new_cheat = cheat - 1
            # else:
            #     new_cheat = cheat

            new_cheat = cheat
            new_item = new_score, nr, nc, new_cheat

            # if (
            #     grid[nr][nc] != "#" or grid[nr][nc] == "#" and new_cheat > 0
            # ) and new_item not in visited:
            #     queue.append(new_item)

            if grid[nr][nc] != "#" and new_item not in visited:
                queue.append(new_item)
                visited.add(new_item)

    return res


def main():
    file = "test_input.txt"
    grid = get_data(file)
    print(grid)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
