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


def get_answer(data):
    return


def main():
    a, b, c, program = get_data("test_input.txt")
    print(a, b, c, program)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
