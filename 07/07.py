def get_rules(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    rules = []
    for line in data:
        value, numbers = line.strip().split(":")
        value = int(value)
        numbers = tuple(map(int, numbers.strip().split()))
        rules.append((value, numbers))
    return rules


def get_answer(data):
    return


def main():
    rules = get_rules("test_input")
    print(rules)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
