from collections import defaultdict


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
                new_group = group + (node,)
                new_group = tuple(sorted(new_group))
                assert len(new_group) == max_len + 1
                groups[max_len + 1].add(new_group)

    return groups


def answer_2(network, groups):
    party_is_found = False
    max_len = max(groups)
    while not party_is_found:
        groups = update_party_info_in_groups(network, groups)
        if max(groups) > max_len:
            max_len = max(groups)
        else:
            party_is_found = True
        # print(f"{groups=}")
        print(f"{max_len=}")
        print(f"{groups[max_len]=}")
    assert len(groups[max_len]) == 1
    return ",".join(list(groups[max_len])[0])


def main():
    file = "test_input.txt"
    network, groups = get_network(file)
    ans2 = answer_2(network, groups)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
