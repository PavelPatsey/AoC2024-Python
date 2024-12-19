import cProfile
from functools import cache


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    towels, designs = data.split("\n\n")
    towels = [x.strip() for x in towels.split(",")]
    designs = designs.split()
    return towels, designs


def is_possible(towels, design):
    @cache
    def dfs(cur_seq, design):
        if not design.startswith(cur_seq):
            return False
        if cur_seq == design:
            return True
        return any((dfs(cur_seq + new_t, design) for new_t in towels))

    return dfs("", design)


def main():
    towels, designs = get_data("input.txt")
    ans1 = sum(map(lambda x: is_possible(towels, x), designs))
    print(ans1)


if __name__ == "__main__":
    cProfile.run("main()")
