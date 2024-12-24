OPERATORS = {
    "AND": "and",
    "OR": "or",
    "XOR": "^",
}


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    wires, gates = data.split("\n\n")
    wires_dict = {}
    for w in wires.splitlines():
        a, b = w.split(":")
        wires_dict[a] = int(b)
    gates_tuples = []
    for g in gates.splitlines():
        w1, op, w2, _, w3 = g.strip().split()
        gates_tuples.append((w1, op, w2, w3))

    return wires_dict, gates_tuples


def all_z_found(all_z, wires):
    return all(map(lambda x: x in wires, all_z))


def execute_operator(x, y, operator):
    if operator == "AND":
        return x and y
    elif operator == "OR":
        return x or y
    elif operator == "XOR":
        return x ^ y
    else:
        raise Exception("Invalid operator")


def get_answer(wires_dict, gates):
    wires = wires_dict.copy()
    all_z = set()
    for gate in gates:
        w1, _, w2, w3 = gate
        if w1.startswith("z"):
            all_z.add(w1)
        if w2.startswith("z"):
            all_z.add(w2)
        if w3.startswith("z"):
            all_z.add(w3)

    print(f"{all_z=}")

    while not all_z_found(all_z, wires):
        for gate in gates:
            w1, op, w2, w3 = gate
            if w1 in wires and w2 in wires and w3 not in wires:
                wires[w3] = execute_operator(wires[w1], wires[w2], op)
                continue

    print(f"{wires=}")
    mapped = list(map(lambda x: (x, wires[x]), all_z))
    print(f"{mapped=}")
    sorted_mapped = sorted(mapped)[::-1]
    print(f"{sorted_mapped=}")
    mapped = list(map(lambda x: x[1], sorted_mapped))
    binary = "".join(str(x) for x in mapped)
    print(f"{binary=}")
    "0011111101000"
    return int(binary, 2)


def main():
    file = "test_input.txt"
    wires, gates = get_data(file)
    ans1 = get_answer(wires, gates)
    print(f"{ans1=}")


if __name__ == "__main__":
    main()
