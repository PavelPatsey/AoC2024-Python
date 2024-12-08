def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in row] for row in data]


def get_antennas_names(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    antennas_names = set()
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] != "." and matrix[r][c] not in antennas_names:
                antennas_names.add(matrix[r][c])
    return antennas_names


def get_answer(matrix, ants_names):
    return


def main():
    matrix = get_matrix("test_input")
    antennas_names = get_antennas_names(matrix)
    print(matrix)
    print(antennas_names)
    print(get_answer(matrix, antennas_names))


if __name__ == "__main__":
    main()
