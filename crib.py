from functools import reduce

DIRS8 = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

DIRS4 = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

DIRS4_dict = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


lst = ["a", "b", "c", "d", "e"]
length = reduce(lambda acc, x: acc + 1, lst, 0)
print(length)


def rotate_clockwise(dir):
    return dir[1], -dir[0]


def rotate_counterclockwise(dir):
    return -dir[1], dir[0]


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols
