import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"


def get_instructions(input_file):
    with open(input_file, "r") as file:
        data = file.read()
        matches = re.findall(pattern, data)
    return matches


def mul(a, b):
    return a * b


def main():
    instructions = get_instructions("input")
    print(instructions)
    print(sum(eval(inst) for inst in instructions))


if __name__ == "__main__":
    main()
