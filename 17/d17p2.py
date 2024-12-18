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


def get_combo(operand, a, b, c):
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


def get_answer(a, b, c, program):
    res = []
    n = len(program)
    i = 0

    while i < n:
        opcode = program[i]
        operand = program[i + 1]
        combo = get_combo(operand, a, b, c)
        if opcode == 0:
            # adv
            a = a // (2**combo)
            i += 2
        elif opcode == 1:
            # bxl
            b = b ^ operand
            i += 2
        elif opcode == 2:
            # bst
            b = combo % 8
            i += 2
        elif opcode == 3:
            # jnz
            if a != 0:
                i = operand
            else:
                i += 2
        elif opcode == 4:
            # bxc
            b = b ^ c
            i += 2
        elif opcode == 5:
            # out
            res.append(combo % 8)
            i += 2
        elif opcode == 6:
            # bdv
            b = a // (2**combo)
            i += 2
        elif opcode == 7:
            # cdv
            c = a // (2**combo)
            i += 2
        else:
            raise Exception(f"Invalid opcode value! {opcode=}")
    return ",".join(map(str, res))


def main():
    a, b, c, program = get_data("input.txt")
    print(a, b, c, program)
    print(get_answer(a, b, c, program))


if __name__ == "__main__":
    main()
