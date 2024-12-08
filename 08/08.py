from collections import defaultdict


def get_matrix(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in row] for row in data]


def get_antennas_coordinates(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    antennas_coordinates = defaultdict(list)
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] != ".":
                antennas_coordinates[matrix[r][c]].append((r, c))
    return antennas_coordinates


def get_answer(matrix, ants_names):
    return


def main():
    matrix = get_matrix("test_input")
    antennas_coordinates = get_antennas_coordinates(matrix)
    print(matrix)
    print(antennas_coordinates)
    print(get_answer(matrix, antennas_coordinates))


if __name__ == "__main__":
    main()
