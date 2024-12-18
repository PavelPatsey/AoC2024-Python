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
    bytes = [tuple(map(int, line.split(","))) for line in data]
    return bytes


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_grid(n, bytes):
    grid = [["." for _ in range(n + 1)] for r in range(n + 1)]
    for c, r in bytes:
        grid[r][c] = "#"
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
    return


def get_answer(n, m, bytes):
    bytes_slice = bytes[0:m]
    grid = get_grid(n, bytes_slice)

    start = 0, 0
    end = n, n

    sr, sc = start
    visited = set()
    queue = deque()
    queue.append((0, sr, sc))

    while queue:
        score, r, c = queue.popleft()
        if (r, c) == end:
            return score
        for dr, dc in DIRS4:
            nr, nc = r + dr, c + dc
            new_score = score + 1
            if (
                in_grid(nr, nc, grid)
                and grid[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                queue.append((new_score, nr, nc))
                visited.add((nr, nc))

    return


def main():
    # n = 6
    # m = 12
    # file = "test_input.txt"

    n = 70
    m = 1024
    file = "input.txt"
    bytes = get_data(file)
    print(get_answer(n, m, bytes))


if __name__ == "__main__":
    main()
