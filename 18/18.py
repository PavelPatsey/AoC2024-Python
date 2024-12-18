def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    bytes = [tuple(map(int, line.split(","))) for line in data]
    return bytes


def get_grid(n):
    return [["." for c in range(n + 1)] for r in range(n + 1)]


def get_answer(data):
    return


def main():
    n = 6  # 6 or 70
    bytes = get_data("test_input.txt")
    print(bytes)
    grid = get_grid(n)
    # print(get_answer(bytes))


if __name__ == "__main__":
    main()
