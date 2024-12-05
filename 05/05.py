from collections import defaultdict
from typing import Dict, Tuple


def get_data(input_file):
    with open(input_file, "r") as file:
        rules, updates = file.read().strip().split("\n\n")
    rules = tuple(
        map(
            lambda x: (int(x[0]), int(x[1])),
            map(lambda x: x.split("|"), rules.splitlines()),
        )
    )
    updates = tuple(
        tuple(int(x) for x in line.split(",")) for line in updates.splitlines()
    )

    return rules, updates


def get_parents(rules: Tuple[int]) -> Dict[int, int]:
    parents = defaultdict(list)
    for k, v in rules:
        parents[v].append(k)
    return parents

    pass


def get_answer(data):
    return


def main():
    rules, updates = get_data("test_input")
    print(rules)
    print(updates)
    parents = get_parents(rules)
    print(parents)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
