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


def is_possible(rule):

    def _is_possible(value, numbers, i, summa):
        if summa > value:
            return False
        if i == len(numbers) - 1:
            return value == summa
        a = summa + numbers[i + 1]
        b = summa * numbers[i + 1]
        return any(
            (
                _is_possible(value, numbers, i + 1, a),
                _is_possible(value, numbers, i + 1, b),
            )
        )

    val, nums = rule
    return _is_possible(val, nums, 0, nums[0])


def is_possible_2(rule):

    def _is_possible_2(value, numbers, i, summa):
        if summa > value:
            return False
        if i == len(numbers) - 1:
            return value == summa
        a = summa + numbers[i + 1]
        b = summa * numbers[i + 1]
        c = int(str(summa) + str(numbers[i + 1]))
        return any(
            (
                _is_possible_2(value, numbers, i + 1, a),
                _is_possible_2(value, numbers, i + 1, b),
                _is_possible_2(value, numbers, i + 1, c),
            )
        )

    val, nums = rule
    return _is_possible_2(val, nums, 0, nums[0])


def get_answer(rules):
    res = 0
    res_2 = 0
    for rule in rules:
        if is_possible(rule):
            res += rule[0]
        if is_possible_2(rule):
            res_2 += rule[0]
    return res, res_2


def main():
    rules = get_rules("input")
    print(rules)
    print(get_answer(rules))


if __name__ == "__main__":
    assert is_possible((190, (10, 19))) is True
    assert is_possible((83, (17, 5))) is False
    main()
