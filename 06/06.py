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


def get_answer(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    start = None
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == "^":
                start = r, c
                break

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


def main():
    matrix = get_matrix("input")
    print(get_answer(matrix))


if __name__ == "__main__":
    main()
