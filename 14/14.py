import re
from collections import Counter, defaultdict
from copy import deepcopy
from functools import reduce
from operator import mul

DIRS4 = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


def get_robots(input_file):
    def _get_robot(string):
        pattern = re.compile(r"-?\d+")
        matches = pattern.findall(string)
        px, py, vx, vy = map(int, matches)
        return (px, py), (vx, vy)

    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [_get_robot(line) for line in data]


def convert_robot(robot):
    p, v = robot
    c, r = p
    dc, dr = v
    new_r = (r + dr) % ROWS
    new_c = (c + dc) % COLS
    return (new_c, new_r), v


def get_quadrant(robot):
    c, r = robot[0]
    rows_mid = ROWS // 2
    cols_mid = COLS // 2
    if r == rows_mid or c == cols_mid:
        return None
    return c < cols_mid, r < rows_mid


def get_answer(robots):
    n = 100
    converted_robots = deepcopy(robots)
    for _ in range(n):
        converted_robots = [convert_robot(r) for r in converted_robots]
    quadrants = [q for r in converted_robots if (q := get_quadrant(r))]
    counter = Counter(quadrants)
    return reduce(mul, counter.values())


def get_grid(coords_set):
    grid = [[" "] * COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            if (c, r) in coords_set:
                grid[r][c] = "#"
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))


def in_grid(c, r):
    return 0 <= r < ROWS and 0 <= c < COLS


def get_robots_coords(robots):
    return {r[0] for r in robots}


def get_groups(robots):
    visited_nodes = set()
    groups = defaultdict(set)
    robots_coords = get_robots_coords(robots)

    def bfs(node):
        visited = {node}
        queue = [node]
        while queue:
            c, r = queue.pop()
            for dc, dr in DIRS4:
                nc, nr = c + dc, r + dr
                if (
                    in_grid(nc, nr)
                    and (nc, nr) not in visited
                    and (nc, nr) in robots_coords
                ):
                    queue.append((nc, nr))
                    visited.add((nc, nr))
        return visited

    for _r in range(ROWS):
        for _c in range(COLS):
            if (_c, _r) not in visited_nodes:
                plot_set = bfs((_c, _r))
                groups[(_c, _r)] = plot_set
                visited_nodes.update(plot_set)

    return groups


def get_answer_2(robots):
    converted_robots = deepcopy(robots)
    for i in range(1, N_MAX):
        if i % 500 == 0:
            print(f"{i=}")
        converted_robots = [convert_robot(r) for r in converted_robots]
        groups = get_groups(converted_robots)
        # g_lens = (len(g) for g in groups.values())
        m_g_lens = max(len(g) for g in groups.values())
        if m_g_lens >= MAX_GROUP_LEN:
            coords_set = get_robots_coords(converted_robots)
            grid = get_grid(coords_set)
            print_grid(grid)
            print(f"{i=} {m_g_lens=}")
            return i
    return


# ROWS, COLS = 7, 11
ROWS, COLS = 103, 101
FILE = "input"

N_MAX = 10_000
MAX_GROUP_LEN = 200


def main():
    robots = get_robots(FILE)
    print(get_answer(robots))
    print(get_answer_2(robots))


if __name__ == "__main__":
    main()
