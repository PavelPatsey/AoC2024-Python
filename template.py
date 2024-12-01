def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def get_answer_1(data):
    return


def main():
    data = get_data("test_input")
    print(data)
    print(get_answer_1(data))


if __name__ == "__main__":
    main()
