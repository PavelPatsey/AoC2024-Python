from collections import defaultdict
from itertools import combinations


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


def get_antinodes(coord_1, coord_2):
    x1, y1 = coord_1
    x2, y2 = coord_2
    dx = x2 - x1
    dy = y2 - y1
    return (x1 - dx, y1 - dy), (x2 + dx, y2 + dy)


def get_answer(matrix, ants_coords):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    antinodes = set()
    for k, v in ants_coords.items():
        coord_pairs = list(combinations(v, 2))
        for coord_1, coord_2 in coord_pairs:
            for ant in get_antinodes(coord_1, coord_2):
                r, c = ant
                if 0 <= r <= ROWS - 1 and 0 <= c <= COLS - 1:
                    antinodes.add(ant)

    return len(antinodes)


def main():
    matrix = get_matrix("input")
    antennas_coordinates = get_antennas_coordinates(matrix)
    print(get_answer(matrix, antennas_coordinates))


if __name__ == "__main__":
    assert get_antinodes((1, 8), (2, 5)) == ((0, 11), (3, 2))
    main()
