from collections import defaultdict
from functools import reduce


def get_network(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    network = defaultdict(set)
    for line in data:
        a, b = line.strip().split("-")
        network[a].add(b)
        network[b].add(a)
    return network


def get_answer(network):
    cons_3 = []
    for node_1 in network.keys():
        for node_2 in network[node_1]:
            for node_3 in network[node_2]:
                if node_3 in network[node_1]:
                    set_3 = {node_1, node_2, node_3}
                    if len(set_3) == 3 and set_3 not in cons_3:
                        cons_3.append(set_3)

    filtered = (
        nodes for nodes in cons_3 if any(map(lambda x: x.startswith("t"), nodes))
    )
    filtered_len = reduce(lambda acc, x: acc + 1, filtered, 0)
    return filtered_len


def main():
    file = "input.txt"
    network = get_network(file)
    ans1 = get_answer(network)
    print(f"{ans1=}")


if __name__ == "__main__":
    main()
