DIRS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


def rotate(dir):
    return dir[0], -dir[1]


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    matrix = [[x for x in row] for row in data]
    return matrix


def get_answer(data):
    return


def main():
    matrix = get_matrix("test_input")
    print(matrix)
    print(get_answer(matrix))


if __name__ == "__main__":
    main()
