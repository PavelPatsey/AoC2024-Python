from collections import defaultdict


def get_connections(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    connections = defaultdict(set)
    for line in data:
        a, b = line.strip().split("-")
        connections[a].add(b)
        connections[b].add(a)
    return connections


def get_answer(connections):
    pass


def main():
    file = "test_input.txt"
    connections = get_connections(file)
    print(connections)
    print(get_answer(connections))


if __name__ == "__main__":
    main()
