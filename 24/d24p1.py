def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    wires, gates = data.split("\n\n")
    wires_dict = {}
    for w in wires.splitlines():
        print(w)
        a, b = w.split(":")
        wires_dict[a] = int(b)
    gates_tuples = []
    for g in gates.splitlines():
        w1, op, w2, _, w3 = g.strip().split()
        gates_tuples.append((w1, op, w2, w3))

    return wires_dict, gates_tuples


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    wires, gates = get_data(file)
    print(wires)
    print(gates)
    # print(get_answer(wires, gates))


if __name__ == "__main__":
    main()
