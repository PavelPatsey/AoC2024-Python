def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    grid, moves = data.split("\n\n")
    grid = grid.split()
    return grid, moves


def get_answer(grid, moves):
    return


def main():
    grid, moves = get_data("test_input.txt")
    print(grid, moves)
    print(get_answer(grid, moves))


if __name__ == "__main__":
    main()
