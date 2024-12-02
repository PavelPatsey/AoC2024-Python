from typing import List


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


def is_safe(report: List[int]) -> bool:
    prev, cur = report[0], report[1]
    sign_r = sign(cur - prev)
    if sign_r == 0:
        return False
    for prev, cur in zip(report, report[1:]):
        if sign(cur - prev) != sign_r or abs(cur - prev) > 3:
            return False
    return True


def main():
    data = get_data("input")
    print(data)
    counter_1 = 0
    for report in data:
        counter_1 += is_safe(report)


if __name__ == "__main__":
    main()
