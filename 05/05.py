from collections import defaultdict
from functools import cmp_to_key
from typing import Dict, List, Tuple


def get_rules_updates(input_file: str) -> Tuple[Dict[int, List[int]], Tuple[int]]:
    def _get_rules_dict(rules_data):
        def _get_rules(rule):
            return tuple(map(int, rule.split("|")))

        rules = map(lambda x: _get_rules(x), rules_data.splitlines())
        rules_dict = defaultdict(list)
        for k, v in rules:
            rules_dict[k].append(v)
        return dict(rules_dict)

    def _get_updates(updates_data):
        return tuple(
            tuple(int(x) for x in line.split(",")) for line in updates_data.splitlines()
        )

    with open(input_file, "r") as file:
        rules_data, updates_data = file.read().strip().split("\n\n")

    return _get_rules_dict(rules_data), _get_updates(updates_data)


def lists_intersect(list1, list2):
    return any(elem in list2 for elem in list1)


def is_correct_update(rules_dict, update):
    prev_pages = []
    for page in update:
        if lists_intersect(rules_dict[page], prev_pages):
            return False
        prev_pages.append(page)
    return True


def get_answer(rules_dict, updates):
    correct_updates = [
        update for update in updates if is_correct_update(rules_dict, update)
    ]
    return sum(map(lambda x: x[len(x) // 2], correct_updates))


def get_correct_update(rules_dict, update):
    def _compare_updates(x, y):
        if y in rules_dict[x]:
            return -1
        return 1

    return sorted(update, key=cmp_to_key(_compare_updates))


def get_answer_2(rules_dict, updates):
    incorrect_updates = [
        update for update in updates if not is_correct_update(rules_dict, update)
    ]
    correct_updates = [
        get_correct_update(rules_dict, update) for update in incorrect_updates
    ]
    return sum(map(lambda x: x[len(x) // 2], correct_updates))


def main():
    rules_dict, updates = get_rules_updates("input")
    print(rules_dict)
    print(updates)
    print(get_answer(rules_dict, updates))
    print(get_answer_2(rules_dict, updates))
    assert get_answer(rules_dict, updates) == 4135
    assert get_answer_2(rules_dict, updates) == 5285


if __name__ == "__main__":
    assert lists_intersect([1, 2], [3, 4]) is False
    assert lists_intersect([1, 2], [2, 4]) is True
    assert lists_intersect([], [2, 4]) is False
    main()
