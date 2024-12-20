import cProfile
import heapq


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                return r, c
    return


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    data = get_data(file)
    print(data)
    print(get_answer(data))


if __name__ == "__main__":
    main()
