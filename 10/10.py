def get_grid(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    grid = [[int(x) if x.isdigit() else -1 for x in line] for line in data]
    return grid


def get_answer(grid):
    return


def main():
    grid = get_grid("test_input_1")
    print(grid)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
