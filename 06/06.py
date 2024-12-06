DIRS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


def rotate(dir):
    return dir[1], -dir[0]


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    matrix = [[x for x in row] for row in data]
    return matrix


def get_start(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    start = None
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == "^":
                start = r, c
                break
    return start


def get_answer(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    start = get_start(matrix)
    r, c = start
    visited = set()
    visited.add(start)
    dir = DIRS["UP"]
    while 0 < r < ROWS - 1 and 0 < c < COLS - 1:
        new = r + dir[0], c + dir[1]
        while matrix[new[0]][new[1]] == "#":
            dir = rotate(dir)
            new = r + dir[0], c + dir[1]
        visited.add(new)
        r, c = new
    return len(visited)


def is_loop(matrix, start, obst):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    dir = DIRS["UP"]
    r, c = start
    visited = set()
    visited.add(start)
    visited_loop = set()
    visited_loop.add((start, dir))
    while 0 < r < ROWS - 1 and 0 < c < COLS - 1:
        new = r + dir[0], c + dir[1]
        while matrix[new[0]][new[1]] == "#" or new == obst:
            dir = rotate(dir)
            new = r + dir[0], c + dir[1]
        visited.add(new)
        if (new, dir) in visited_loop:
            return True
        visited_loop.add((new, dir))
        r, c = new
    return False


def get_answer_2(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    start = get_start(matrix)
    counter = 0
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) != start:
                if is_loop(matrix, start, (r, c)):
                    counter += 1
                    print(f"{counter=}")
    return counter


def main():
    matrix = get_matrix("input")
    print(get_answer(matrix))
    print(get_answer_2(matrix))


if __name__ == "__main__":
    main()
