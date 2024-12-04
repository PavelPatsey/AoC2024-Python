def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def convert_data(data):
    xmas_set = {"X", "M", "A", "S"}
    converted_data = []
    for line in data:
        converted_line = []
        for char in line:
            if char in xmas_set:
                converted_line.append(char)
            else:
                converted_line.append(".")
        converted_data.append(converted_line)

    row = ["."] * (len(data[0]) + 6)
    extended = [row, row, row]

    for line in converted_data:
        extended.append(["."] * 3 + line + ["."] * 3)
    extended.extend([row, row, row])

    return extended


def get_answer_1(data):
    return


def main():
    data = get_data("test_input")
    print(data)
    converted_data = convert_data(data)
    print(converted_data)
    # print(get_answer_1(data))


if __name__ == "__main__":
    main()
