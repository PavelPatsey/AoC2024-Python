import cProfile
from functools import cache


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    towels, designs = data.split("\n\n")
    towels = [x.strip() for x in towels.split(",")]
    designs = designs.split()
    return towels, designs


def ways_number(towels, design):
    @cache
    def recursion(tail: str):
        if tail == "":
            return 1
        n = 0
        for t in towels:
            if tail.startswith(t):
                new_tail = tail[len(t) :]
                n += recursion(new_tail)
        return n

    res = recursion(design)
    return res


def get_answer(towels, designs):
    return sum(map(lambda x: ways_number(towels, x), designs))


def main():
    towels, designs = get_data("input.txt")
    print(get_answer(towels, designs))


if __name__ == "__main__":
    cProfile.run("main()")
