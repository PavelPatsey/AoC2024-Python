import re
from collections import Counter
from copy import deepcopy
from functools import reduce
from operator import mul


def get_robots(input_file):
    def _get_robot(string):
        "p=0,4 v=3,-3"
        pattern = re.compile(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)")
        matches = pattern.findall(string)
        px, py, vx, vy = map(int, matches[0])
        return (px, py), (vx, vy)

    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [_get_robot(line) for line in data]


def get_grid():
    return [[0] * COLS for _ in range(ROWS)]


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

    res = c < cols_mid, r < rows_mid
    return c < cols_mid, r < rows_mid


def get_answer(robots):
    n = 100
    converted_robots = deepcopy(robots)
    for _ in range(n):
        converted_robots = [convert_robot(r) for r in converted_robots]
    quadrants = [q for r in converted_robots if (q := get_quadrant(r))]
    counter = Counter(quadrants)
    return reduce(mul, counter.values())


# ROWS, COLS = 7, 11  # 7, 11 or 103, 101
ROWS, COLS = 103, 101  # 7, 11 or 103, 101
FILE = "input"


def main():
    robots = get_robots(FILE)
    print(get_answer(robots))


if __name__ == "__main__":
    main()
