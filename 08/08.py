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


def in_matrix(node, rows, cols):
    r, c = node
    return 0 <= r < rows and 0 <= c < cols


def get_antinodes(node_1, node_2, rows, cols):
    x1, y1 = node_1
    x2, y2 = node_2
    dx = x2 - x1
    dy = y2 - y1
    antinodes = set()
    new_node_1 = x1 - dx, y1 - dy
    if in_matrix(new_node_1, rows, cols):
        antinodes.add(new_node_1)
    new_node_2 = x2 + dx, y2 + dy
    if in_matrix(new_node_2, rows, cols):
        antinodes.add(new_node_2)
    return antinodes


def get_answer(matrix, ants_coords):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    antinodes = set()
    for v in ants_coords.values():
        for node_1, node_2 in combinations(v, 2):
            antinodes.update(get_antinodes(node_1, node_2, ROWS, COLS))

    return len(antinodes)


def get_antinodes_2(node_1, node_2, rows, cols):
    antinodes = set()
    r1, c1 = node_1
    r2, c2 = node_2
    dr = r2 - r1
    dc = c2 - c1

    i = 1
    new_r1 = r1 - i * dr
    new_c1 = c1 - i * dc
    while in_matrix((new_r1, new_c1), rows, cols):
        antinodes.add((new_r1, new_c1))
        i += 1
        new_r1 = r1 - i * dr
        new_c1 = c1 - i * dc

    i = 1
    new_r2 = r2 + i * dr
    new_c2 = c2 + i * dc
    while in_matrix((new_r2, new_c2), rows, cols):
        antinodes.add((new_r2, new_c2))
        i += 1
        new_r2 = r2 + i * dr
        new_c2 = c2 + i * dc

    return antinodes


def get_answer_2(matrix, ants_coords):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    antinodes = set()
    for v in ants_coords.values():
        for node_1, node_2 in combinations(v, 2):
            antinodes.add(node_1)
            antinodes.add(node_2)
            antinodes.update(get_antinodes_2(node_1, node_2, ROWS, COLS))

    return len(antinodes)


def main():
    matrix = get_matrix("input")
    antennas_coordinates = get_antennas_coordinates(matrix)
    print(get_answer(matrix, antennas_coordinates))
    print(get_answer_2(matrix, antennas_coordinates))


if __name__ == "__main__":
    main()
