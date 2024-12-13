import re

A_PRICE = 3
B_PRICE = 1
ADDITION = 10000000000000


def get_machines(input_file):
    def _get_machine(s):
        "Button A: X+94, Y+34\nButton B: X+22, Y+67\nPrize: X=8400, Y=5400'"
        a_str, b_str, prize_str = s.strip().split("\n")
        a = re.split(r"[+,]", a_str)
        a = int(a[-3]), int(a[-1])
        b = re.split(r"[+,]", b_str)
        b = int(b[-3]), int(b[-1])
        p = re.split(r"[=,]", prize_str)
        p = int(p[-3]), int(p[-1])
        return a, b, p

    with open(input_file, "r") as file:
        data = file.read().strip().split("\n\n")
    machines = list(map(_get_machine, data))
    return machines


def f(a, b, p):
    x1, y1 = a
    x2, y2 = b
    x, y = p
    c2 = y2 * x1 - x2 * y1
    if c2 == 0:
        return
    c1 = y * x1 - x * y1
    if not c1 % c2 == 0:
        return
    b = c1 // c2
    if not (x - b * x2) % x1 == 0:
        return
    a = (x - b * x2) // x1
    return a, b


def get_answer(machines):
    res = 0
    for m in machines:
        a, b, p = m
        sol = f(a, b, p)
        if sol:
            res += sol[0] * A_PRICE + sol[1] * B_PRICE
    return res


def get_answer_2(machines):
    res = 0
    for m in machines:
        a, b, p = m
        p2 = p[0] + ADDITION, p[1] + ADDITION
        sol = f(a, b, p2)
        if sol:
            res += sol[0] * A_PRICE + sol[1] * B_PRICE
    return res


def main():
    machines = get_machines("input")
    print(get_answer(machines))
    print(get_answer_2(machines))


if __name__ == "__main__":
    main()
