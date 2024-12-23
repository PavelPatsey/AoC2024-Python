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
    cons_3 = []
    for node_1, nbrs_1 in connections.items():
        set_1 = {node_1}
        for node_2 in connections[node_1]:
            set_2 = set_1 | {node_2}
            for node_3 in connections[node_2]:
                if node_3 in connections[node_1]:
                    set_3 = set_2 | {node_3}
                    if len(set_3) == 3 and set_3 not in cons_3:
                        cons_3.append(set_3)

    print(cons_3)
    print(len(cons_3))

    for n1, n2, n3 in cons_3:
        assert n1 in connections[n2] and n1 in connections[n3]
        assert n2 in connections[n1] and n1 in connections[n3]
        assert n3 in connections[n1] and n1 in connections[n2]

    filtered = []
    for nodes in cons_3:
        if any(map(lambda x: x.startswith("t"), nodes)):
            filtered.append(nodes)

    print(filtered)
    print(len(filtered))
    return len(filtered)


def main():
    file = "test_input.txt"
    connections = get_connections(file)
    print(connections)
    ans1 = get_answer(connections)
    print(f"{ans1=}")


if __name__ == "__main__":
    main()
