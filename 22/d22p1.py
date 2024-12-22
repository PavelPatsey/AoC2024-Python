from collections import defaultdict


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [int(x) for x in data]


def mix(x, y):
    return x ^ y


def prune(x):
    return x % 16777216


def convert(x):
    y = prune(mix(x, x * 64))
    y = prune(mix(y, y // 32))
    y = prune(mix(y, y * 2048))
    return y


def get_answer(numbers, n):
    res = numbers.copy()
    for _ in range(n):
        res = map(convert, res)
    return sum(res)


def make_price(x):
    return int(str(x)[-1])


def f(x):
    p0, p1, p2, p3, p4 = x
    mask = p1 - p0, p2 - p1, p3 - p2, p4 - p3
    return p4, mask


def get_changes(number, n):
    secret_numbers = [number]
    conv_number = number
    for _ in range(n):
        conv_number = convert(conv_number)
        secret_numbers.append(conv_number)
    # print(f"{secret_numbers=}")
    prices = list(map(make_price, secret_numbers))
    print(f"{prices=}")
    print(f"{len(prices)=}")

    changes = []
    masks_set = set()
    for p in zip(prices, prices[1:], prices[2:], prices[3:], prices[4:]):
        price, mask = f(p)
        if mask not in masks_set:
            changes.append((price, mask))
            masks_set.add(mask)
    print(f"{changes=}")
    print(f"{len(changes)=}")
    return changes


def get_answer_2(numbers, n):
    my_dict = defaultdict(int)
    for num in numbers:
        changes = get_changes(num, n)
        for price, mask in changes:
            my_dict[mask] += price

    max_mask = None
    max_price = 0
    for mask, price in my_dict.items():
        if price > max_price:
            max_mask = mask
            max_price = price
    print(f"{max_mask=}")
    print(f"{max_price=}")
    return max_price


def main():
    file = "test_input_2.txt"
    secret_numbers = get_data(file)
    # asn1 = get_answer(secret_numbers, 2000)
    # print(f"{asn1=}")
    asn2 = get_answer_2(secret_numbers, 2000)
    print(f"{asn2=}")


if __name__ == "__main__":
    assert mix(15, 42) == 37
    assert prune(100000000) == 16113920
    assert convert(123) == 15887950
    assert convert(convert(123)) == 16495136

    assert make_price(123) == 3
    assert make_price(15887950) == 0

    assert (6, (-1, -1, 0, 2)) in get_changes(123, 10)
    assert (7, (-2, 1, -1, 3)) in get_changes(1, 2_000)
    assert (7, (-2, 1, -1, 3)) in get_changes(2, 2_000)
    assert (9, (-2, 1, -1, 3)) in get_changes(2024, 2_000)
    main()
