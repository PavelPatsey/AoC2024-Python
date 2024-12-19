def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    data = get_data(file)
    print(data)
    print(get_answer(data))


if __name__ == "__main__":
    main()
