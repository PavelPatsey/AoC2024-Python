from typing import List

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


def get_data(input_file) -> List[str]:
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def get_extended_matrix(data: List[str]) -> List[List[str]]:
    converted_data = [[char for char in line] for line in data]
    row = ["."] * (len(data[0]) + 6)
    extended = [row, row, row]
    for line in converted_data:
        extended.append(["."] * 3 + line + ["."] * 3)
    extended.extend([row, row, row])
    return extended


def get_answer_1(matrix):
    def _xmas_appears_number(r: int, c: int) -> int:
        counter = 0
        xmas = ["X", "M", "A", "S"]
        n = len(xmas)
        for d in DIRS8:
            candidate = [matrix[r + i * d[0]][c + i * d[1]] for i in range(n)]
            if candidate == xmas:
                counter += 1
        return counter

    res = 0
    for row in range(3, len(matrix) - 3):
        for col in range(3, len(matrix[0]) - 3):
            res += _xmas_appears_number(row, col)
    return res


def get_answer_2(matrix):
    def is_mas_appears(r: int, c: int) -> bool:
        mas = ["M", "A", "S"]
        n = len(mas)
        d = (1, 1)
        candidate_1 = [matrix[r + i * d[0]][c + i * d[1]] for i in range(n)]
        d = (1, -1)
        candidate_2 = [matrix[r + i * d[0]][c + 2 + i * d[1]] for i in range(n)]
        return (candidate_1 == mas or candidate_1 == mas[::-1]) and (
            candidate_2 == mas or candidate_2 == mas[::-1]
        )

    res = 0
    for row in range(3, len(matrix) - 3):
        for col in range(3, len(matrix[0]) - 3):
            if is_mas_appears(row, col):
                res += 1
    return res


def main():
    data = get_data("input")
    extended_matrix = get_extended_matrix(data)
    print(get_answer_1(extended_matrix))
    print(get_answer_2(extended_matrix))


if __name__ == "__main__":
    main()
