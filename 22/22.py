def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [int(x) for x in data]


def get_answer(numbers):
    return


def main():
    file = "test_input.txt"
    secret_numbers = get_data(file)
    print(secret_numbers)
    print(get_answer(secret_numbers))


if __name__ == "__main__":
    main()
