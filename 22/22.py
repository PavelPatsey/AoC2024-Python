def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [int(x) for x in data]


def mix(x, y):
    return x ^ y


def prune(x):
    return x % 16777216


def convert(x):
    y = prune(mix(x, x * 64))
    y = prune(mix(y, y // 32))
    y = prune(mix(y, y * 2048))
    return y


def get_answer(numbers):
    return


def main():
    file = "test_input.txt"
    secret_numbers = get_data(file)
    print(secret_numbers)
    print(get_answer(secret_numbers))


if __name__ == "__main__":
    assert mix(15, 42) == 37
    assert prune(100000000) == 16113920
    assert convert(123) == 15887950
    main()
