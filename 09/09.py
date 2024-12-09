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


def get_l(blocks, l=0):
    while blocks[l] != ".":
        l += 1
    return l


def get_dl(blocks, l):
    dl = 0
    while l + dl < len(blocks) and blocks[l + dl] == ".":
        dl += 1
    return dl


def get_r(blocks, ind=None):
    r = ind if ind else len(blocks) - 1
    while blocks[r] == ".":
        r -= 1
    return r


def get_dr(blocks, r):
    dr = 0
    while blocks[r - dr] == blocks[r]:
        dr += 1
    return dr


def get_answer_2(disk_map):
    blocks = get_blocks(disk_map)
    r = get_r(blocks)
    while r > 0:
        l = get_l(blocks)
        dl = get_dl(blocks, l)
        r = get_r(blocks, r)
        dr = get_dr(blocks, r)
        is_swapped = False
        while l < r and not is_swapped:
            if dl >= dr:
                for i in range(dr):
                    blocks[l + i], blocks[r - i] = blocks[r - i], blocks[l + i]
                l += dr
                is_swapped = True
            else:
                l += dl
                l = get_l(blocks, l)
                dl = get_dl(blocks, l)
        r -= dr

    res = 0
    for i, x in enumerate(blocks):
        if x != ".":
            res += i * x
    return res


def main():
    disk_map = get_disk_map("input")
    print(get_answer(disk_map))
    print(get_answer_2(disk_map))


if __name__ == "__main__":
    main()
