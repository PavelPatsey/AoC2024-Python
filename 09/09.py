def get_disk_map(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    data = [int(x) for x in data]
    return data


def get_blocks(disk_map):
    blocks = []
    c = 0
    for i, d in enumerate(disk_map):
        if i % 2 == 0:
            blocks.extend([c] * disk_map[i])
            c += 1
        else:
            blocks.extend(["."] * d)
    return blocks


def get_answer(disk_map):
    blocks = get_blocks(disk_map)
    l, r = 0, len(blocks) - 1
    while blocks[r] == ".":
        r -= 1
    while l < r and not blocks[r] == ".":
        if blocks[l] == ".":
            blocks[l], blocks[r] = blocks[r], blocks[l]
            r -= 1
            while blocks[r] == ".":
                r -= 1
        l += 1

    filtered = filter(lambda x: x != ".", blocks)
    mapped = map(lambda x: x[0] * x[1], enumerate(filtered))
    return sum(mapped)


def main():
    disk_map = get_disk_map("input")
    print(get_answer(disk_map))


if __name__ == "__main__":
    main()
