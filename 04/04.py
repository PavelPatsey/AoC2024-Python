from typing import List, Tuple

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

EN = 3


def get_data(input_file) -> List[str]:
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def get_extended_matrix(data: List[str]) -> List[List[str]]:
    converted_data = [[char for char in line] for line in data]
    row = ["."] * (len(data[0]) + 2 * EN)
    extended = [row for _ in range(EN)]
    for line in converted_data:
        extended.append(["."] * EN + line + ["."] * EN)
    extended.extend([row for _ in range(EN)])
    return extended


def get_answer(matrix: List[List[str]]) -> Tuple[int]:
    def _xmas_appears_number(r: int, c: int) -> int:
        counter = 0
        xmas = ["X", "M", "A", "S"]
        n = len(xmas)
        for d in DIRS8:
            candidate = [matrix[r + i * d[0]][c + i * d[1]] for i in range(n)]
            if candidate == xmas:
                counter += 1
        return counter

    def _is_x_mas_appears(r: int, c: int) -> bool:
        mas = ["M", "A", "S"]
        n = len(mas)
        d = (1, 1)
        candidate_1 = [matrix[r + i * d[0]][c + i * d[1]] for i in range(n)]
        if candidate_1 != mas and candidate_1 != mas[::-1]:
            return False
        d = (1, -1)
        candidate_2 = [matrix[r + i * d[0]][c + 2 + i * d[1]] for i in range(n)]
        return candidate_2 == mas or candidate_2 == mas[::-1]

    res_1, res_2 = 0, 0
    for row in range(EN, len(matrix) - EN):
        for col in range(EN, len(matrix[0]) - EN):
            res_1 += _xmas_appears_number(row, col)
            if _is_x_mas_appears(row, col):
                res_2 += 1
    return res_1, res_2


def main():
    data = get_data("input")
    extended_matrix = get_extended_matrix(data)
    print(get_answer(extended_matrix))


if __name__ == "__main__":
    main()
