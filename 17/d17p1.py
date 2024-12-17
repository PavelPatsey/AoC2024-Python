import re

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

OPERANDS = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: "A",
    5: "B",
    6: "C",
}


def get_operand(opr, a, b, c):
    if 0 <= opr <= 3:
        return opr
    elif opr == 4:
        return a
    elif opr == 5:
        return b
    elif opr == 6:
        return c
    else:
        raise Exception("Invalid operand value")


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


def get_answer(a, b, c, program):
    return


def main():
    a, b, c, program = get_data("test_input.txt")
    print(a, b, c, program)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
