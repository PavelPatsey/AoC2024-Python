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


def get_answer_1(extended_data):
    LEN_ROWS = len(extended_data)
    LEN_COLS = len(extended_data[0])
    for r in range(3, LEN_ROWS - 3):
        for c in range(3, LEN_COLS - 3):
            print(extended_data[r])


def main():
    data = get_data("test_input")
    # print(data)
    extended_data = extend_data(data)
    # print(converted_data)
    print(get_answer_1(extended_data))


if __name__ == "__main__":
    main()
