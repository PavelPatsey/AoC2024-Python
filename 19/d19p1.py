def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    towels, designs = data.split("\n\n")
    towels = [x.strip() for x in towels.split(",")]
    designs = designs.split()
    return towels, designs


def dfs(t, towels, cur_seq, design: str):
    if not design.startswith(cur_seq):
        return
    if cur_seq == design:
        return cur_seq




def get_answer(towels, designs):
    for d in designs


def main():
    towels, designs = get_data("test_input.txt")
    print(towels, designs)
    print(get_answer(towels, designs))


if __name__ == "__main__":
    main()
