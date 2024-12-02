from typing import List


def get_reports(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[int(x) for x in d.split()] for d in data]


def sign(x: int) -> int:
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


def is_safe_2(report: List[int]) -> bool:
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def main():
    reports = get_reports("input")
    print(reports)
    counter_1 = 0
    counter_2 = 0
    for report in reports:
        counter_1 += is_safe(report)
        counter_2 += is_safe_2(report)
    print(counter_1)
    print(counter_2)


if __name__ == "__main__":
    main()
