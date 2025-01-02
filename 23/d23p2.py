from collections import defaultdict
from functools import reduce


def get_network(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    network = defaultdict(set)
    groups = defaultdict(set)
    for line in data:
        a, b = line.strip().split("-")
        network[a].add(b)
        network[b].add(a)
        groups[2].add(tuple(sorted([a, b])))
    return network, groups


def update_party_info_in_groups(network, groups):
    max_len = max(groups)

    for node in network:
        for group in groups[max_len]:
            if node not in group and all(map(lambda x: node in network[x], group)):
                new_group = set(group) | {node}
                new_group = tuple(sorted(new_group))
                assert len(new_group) == max_len + 1
                groups[max_len + 1].add(new_group)

    return groups


def answer_2(network, groups):
    groups = update_party_info_in_groups(network, groups)
    filtered = (
        nodes for nodes in groups[3] if any(map(lambda x: x.startswith("t"), nodes))
    )
    filtered_len = reduce(lambda acc, x: acc + 1, filtered, 0)
    return filtered_len


def main():
    file = "input.txt"
    network, groups = get_network(file)
    ans2 = answer_2(network, groups)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
