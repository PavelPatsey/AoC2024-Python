def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    towels, designs = data.split("\n\n")
    towels = [x.strip() for x in towels.split(",")]
    designs = designs.split()
    return towels, designs


def get_answer(towels, designs):
    return


def main():
    towels, designs = get_data("test_input.txt")
    print(towels, designs)
    print(get_answer(towels, designs))


if __name__ == "__main__":
    main()
