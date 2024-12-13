import re


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


def get_answer(data):
    return


def main():
    machines = get_machines("test_input")
    print(machines)
    # print(get_answer(machines))


if __name__ == "__main__":
    main()
