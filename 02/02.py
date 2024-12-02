def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
        res = []
        for d in data:
            res.append([int(x) for x in d.split()])
    return res


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def f(lst):
    counter = 0
    for x in lst[1:]:
        if sign(x) == sign(lst[0]) and abs(x) <= 3:
            counter += 1
    return counter == len(lst) - 1


def get_answer_1(data):
    converted = []
    for d in data:
        converted.append([b - a for a, b in zip(d, d[1:])])
    print(converted)
    filtered = [f(x) for x in converted]
    print(filtered)
    return sum(filtered)


def main():
    data = get_data("input")
    print(data)
    print(get_answer_1(data))


if __name__ == "__main__":
    main()
