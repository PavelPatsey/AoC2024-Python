DIRS = [
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def extend_data(data):
    converted_data = [[char for char in line] for line in data]
    row = ["."] * (len(data[0]) + 6)

    extended = [row, row, row]
    for line in converted_data:
        extended.append(["."] * 3 + line + ["."] * 3)
    extended.extend([row, row, row])

    return extended


def get_answer_1(matrix):
    def _xmas_appears_number(r, c):
        counter = 0
        xmas = ["X", "M", "A", "S"]
        for dir in DIRS:
            pretentend = [matrix[r + i * dir[0]][c + i * dir[1]] for i in range(4)]
            if pretentend == xmas:
                counter += 1

        return counter

    LEN_ROWS = len(matrix)
    LEN_COLS = len(matrix[0])

    res = 0
    _xmas_appears_number(3, 3)
    for row in range(3, LEN_ROWS - 3):
        for col in range(3, LEN_COLS - 3):
            res += _xmas_appears_number(row, col)
    return res


def main():
    data = get_data("input")
    extended_data = extend_data(data)
    print(get_answer_1(extended_data))


if __name__ == "__main__":
    main()
