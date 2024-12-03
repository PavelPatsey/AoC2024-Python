import re


def get_instructions(input_file):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    with open(input_file, "r") as file:
        data = file.read()
        matches = re.findall(pattern, data)
    return matches


def get_instructions_2(input_file):
    pattern = r"^mul\(\d{1,3},\d{1,3}\)"
    with open(input_file, "r") as file:
        data = file.read()
    instructions = []
    for i, char in enumerate(data):
        if char == "m":
            match = re.match(pattern, data[i:])
            if match:
                instructions.append(match.group())
        elif char == "d":
            if data[i:].startswith("do()"):
                instructions.append("do()")
            elif data[i:].startswith("don't()"):
                instructions.append("don't()")

    return instructions


def mul(a, b):
    return a * b


def get_answer_2(instructions):
    enable = True
    res = 0
    for inst in instructions:
        if inst == "don't()":
            enable = False
            continue
        elif inst == "do()":
            enable = True
            continue

        if enable:
            res += eval(inst)
    return res


def main():
    instructions = get_instructions("test_input")
    # print(instructions)
    # print(sum(eval(inst) for inst in instructions))
    instructions_2 = get_instructions_2("input")
    print(instructions_2)
    print(get_answer_2(instructions_2))


if __name__ == "__main__":
    main()
