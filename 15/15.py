from copy import deepcopy
from collections import defaultdict

DIRS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

CONVERTS = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    grid, moves = data.split("\n\n")
    grid = grid.split()
    grid = [[x for x in line] for line in grid]
    moves = moves.strip()
    moves = "".join(moves.split())
    return grid, moves


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()
    return


def get_start(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                return r, c
    return


def convert(grid, move, node):
    dir = DIRS[move]

    def do_move(pos):
        r, c = pos
        dr, dc = dir
        nr, nc = r + dr, c + dc
        new_pos = nr, nc
        if grid[nr][nc] == ".":
            grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
            return True
        elif grid[nr][nc] == "O":
            moved = do_move(new_pos)
            if moved:
                grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
                return True
            return False
        elif grid[nr][nc] == "#":
            return False
        else:
            raise Exception(f"invalid case! {grid[nr][nc]=}")

    is_moved = do_move(node)
    r, c = node
    new_node = node
    if is_moved:
        dr, dc = dir
        new_node = r + dr, c + dc
    return grid, new_node


def get_score(grid):
    res = 0
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "O":
                res += r * 100 + c
    return res


def get_answer(grid, moves, start):
    node = start
    converted_grid = deepcopy(grid)
    for move in moves:
        converted_grid, node = convert(converted_grid, move, node)

    return get_score(converted_grid)


def get_extended_grid(grid):
    extended_grid = []
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        new_row = []
        for c in range(cols):
            node = grid[r][c]
            new_row.extend([x for x in CONVERTS[node]])
        extended_grid.append(new_row)
    return extended_grid


def in_grid(node, grid):
    r, c = node
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_box(node, grid):
    if not in_grid(node, grid):
        return
    r, c = node
    if grid[r][c] == "[":
        left = r, c
        right = r, c + 1
    elif grid[r][c] == "]":
        right = r, c
        left = r, c - 1
    else:
        return
    return left, right


def get_boxes_dict(grid, move, next_n):
    print(next_n)
    dir = DIRS[move]
    # dr, dc = dir
    boxes_dict = defaultdict(set)
    box = get_box(next_n, grid)
    assert box is not None
    queue = [box]
    while queue:
        box = queue.pop()
        left, right = box
        if move in {"^", "v"}:
            next_nodes = box
        elif move == "<":
            next_nodes = [(left[0], left[1] - 2)]
        elif move == ">":
            next_nodes = [(left[0], left[1] + 2)]
        for next_n in next_nodes:
            nr, nc = next_n

            if new_box := get_box((nr, nc), grid):
                # visited.add(new_box)
                queue.append(new_box)
                boxes_dict[box].add(new_box)
    return boxes_dict


def get_new_grid(get_boxes_to_move):
    pass


def get_converted_2(grid, move, node):
    # "<" ">" "^" "v"
    r, c = node
    dir = DIRS[move]
    dr, dc = dir
    nr, nc = r + dr, c + dc
    new_node = nr, nc

    if grid[nr][nc] == ".":
        grid[r][c], grid[nr][nc] = grid[nr][nc], grid[r][c]
        return grid, new_node
    elif grid[nr][nc] in {"[", "]"}:
        boxes_dict = get_boxes_dict(grid, move, new_node)
        print_grid(grid)
        # print(f"{(grid, move, node)=}")
        print(f"{boxes_dict=}")
        assert False
        new_grid = get_new_grid(get_boxes_dict)
        return new_grid, new_node
    elif grid[nr][nc] == "#":
        return grid, node
    else:
        raise Exception(f"invalid case! {grid[nr][nc]=}")


def get_answer_2(grid, moves):
    node = get_start(grid)
    new_node = node
    converted_grid = deepcopy(grid)
    for move in moves:
        converted_grid, new_node = get_converted_2(converted_grid, move, new_node)
        print_grid(converted_grid)

    return get_score(converted_grid)


def main():
    grid, moves = get_data("input_2_part.txt")
    # start = get_start(grid)
    #
    # ans1 = get_answer(grid, moves, start)
    # print(f"{ans1=}")

    extended_grid = get_extended_grid(grid)

    print("Initial state:")
    print_grid(extended_grid)

    ans2 = get_answer_2(extended_grid, moves)
    print(f"{ans2=}")


if __name__ == "__main__":
    main()
