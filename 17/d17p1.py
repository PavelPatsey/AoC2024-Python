import re


def get_data(input_file):
    pattern = re.compile(r"\d+", re.MULTILINE)

    with open(input_file, "r") as file:
        data = file.read().strip()
    registers, program = data.split("\n\n")
    registers = pattern.findall(registers)
    a, b, c = list(map(int, registers))
    program = pattern.findall(program)
    program = list(map(int, program))
    return a, b, c, program


def get_combo_operand(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        raise Exception("Invalid operand value")


def adv(operand, a, b, c):
    combo = get_combo_operand(operand, a, b, c)
    res = a // (2 ^ combo)
    a = res
    return res, a, b, c


def bxl(operand, a, b, c):
    res = b ^ operand
    b = res
    return res, a, b, c


def bst(operand, a, b, c):
    combo = get_combo_operand(operand, a, b, c)
    res = combo % 8
    b = res
    return res, a, b, c


def jnz(operand, a, b, c):
    if a != 0:
        res = operand
    else:
        res += 2


OPCODES = {
    0: "adv",
    1: "bxl",
    2: "bst",
    3: "jnz",
    4: "bxc",
    5: "out",
    6: "bdv",
    7: "cdv",
}


def do_instruction(opcode, operand, a, b, c):
    return res, a, b, c


def get_answer(a, b, c, program):
    res = []
    n = len(program)
    i = 0

    while i < n:
        opcode = program[i]
        operand = program[i + 1]
        if i == 0:
            # adv
            combo = get_combo_operand(operand, a, b, c)
            res = a // (2 ^ combo)
            a = res


def main():
    a, b, c, program = get_data("test_input.txt")
    print(a, b, c, program)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
