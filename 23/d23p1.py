def get_connections(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    connections = [tuple(x.strip().split("-")) for x in data]
    return connections


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    connections = get_connections(file)
    print(connections)
    print(get_answer(connections))


if __name__ == "__main__":
    main()
